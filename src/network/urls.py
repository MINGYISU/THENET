
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("newpost", views.create, name="newpost"), 
    path("profile/<int:identity>", views.show_profile, name="profile"), 
    path("following", views.show_flwing, name="following"), 
    path("togflw", views.toggle_flw, name="togflw"), 
    path("like", views.like, name="like")
]
