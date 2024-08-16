from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Follower, Like

import json

def index(request):
    return render(request, "network/index.html", {
        "posts": Post.objects.all()[::-1]
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html", {
            "next": request.GET.get('next', '')
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def create(request):
    user = request.user
    if request.method == "POST":
        content = request.POST["content"]
        post = Post(poster=user, content=content)
        post.save()
        user.add_pts()
        user.save()

        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'network/newpost.html', {
            "posts": Post.objects.all()
        })

def show_profile(request, identity):
    user = get_object_or_404(User, id=identity)
    return render(request, "network/profile.html", {
        "watching": user
    })

@login_required
def show_flwing(request):
    user = request.user
    idols = Follower.objects.filter(fan=user)
    idols = [ele.idol for ele in idols]
    return render(request, 'network/index.html', {
        "is_flwing_page": True, 
        "posts": sorted(Post.objects.filter(poster__in=idols), key=lambda x: x.time)
    })
    
@login_required
@require_POST
def toggle_flw(request):
    user = request.user
    data = json.loads(request.body)
    IdolID = data.get('IdolID')
    to_flw = get_object_or_404(User, id=IdolID)
    if user.id == to_flw.id:
        return Http404("Invalid! You cannot follow yourself!")
    
    # Check if user is following the user to follow
    is_flwing = Follower.objects.filter(idol=to_flw, fan=user).exists()

    # if the user is not following the idol to follow, add that idol
    if not is_flwing:
        new_fan = Follower(idol=to_flw, fan=user)
        new_fan.save()
        user.add_flwing()
        user.save()
        to_flw.add_flwer()
        to_flw.save()
        return JsonResponse({"success": True, "flwed": True, "n_flwer": to_flw.flwers})
    # else remove that idol
    else:
        del_fan = Follower.objects.get(idol=to_flw, fan=user)
        del_fan.delete()
        user.del_flwing()
        user.save()
        to_flw.del_flwer()
        to_flw.save()
        return JsonResponse({"success": True, "flwed": False, "n_flwer": to_flw.flwers})

    # In case of error
    return JsonResponse({"success": False}, status=403)

@login_required
@require_POST
def like(request):
    user = request.user
    data = json.loads(request.body)
    pt_id = data.get('postid')
    to_like = get_object_or_404(Post, id=pt_id)

    # Check if the user already liked the post
    is_liking = Like.objects.filter(liking=to_like, liker=user).exists()

    if not is_liking:
        new_like = Like(liking=to_like, liker=user)
        new_like.save()
        to_like.add_likes()
        to_like.save()
        return JsonResponse({"success": True, "liked": True, "n_liker": to_like.likes})
    else:
        del_like = Like.objects.get(liking=to_like, liker=user)
        del_like.delete()
        to_like.unlike()
        to_like.save()
        return JsonResponse({"success": True, "liked": False, "n_liker": to_like.likes})

    return JsonResponse({"success": False}, status=403)

@login_required
@require_POST
def edit_post(request, identity):
    user = request.user
    to_update = Post.objects.get(id=identity)

    if user.id != to_update.poster.id:
        return JsonResponse({"success": False, "NOTMYSELF": True})

    data = json.loads(request.body)
    updated = data.get("updated")
    to_update.content = updated
    to_update.save()

    return JsonResponse({"success": True, "updated": to_update.content})

