from django import template
from network.models import User, Post, Follower, Like

register = template.Library()

@register.simple_tag
def get_len_posts(user):
    return len(Post.objects.filter(poster=user))

@register.simple_tag
def get_len_flwers(user):
    return len(user.idols.all())

@register.simple_tag
def get_len_flwings(user):
    return len(user.fans.all())

@register.simple_tag
def get_posts_for(user):
    return Post.objects.filter(poster=user)[::-1]

@register.simple_tag
def is_myself(u1, u2):
    return u1.id == u2.id

@register.simple_tag
def is_flwing(u1, u2):
    return Follower.objects.filter(idol=u1, fan=u2).exists()

@register.simple_tag
def is_liking(post, user=None):
    return Like.objects.filter(liking=post, liker=user).exists()