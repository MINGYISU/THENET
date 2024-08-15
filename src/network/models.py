from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    joined_at = models.DateTimeField(auto_now_add=True)
    pts = models.IntegerField(default=0)
    flwers = models.IntegerField(default=0)
    flwings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.username}"

    def add_pts(self):
        self.pts += 1

    def add_flwer(self):
        self.flwers += 1

    def del_flwer(self):
        assert(self.flwers >= 0)
        if self.flwers > 0:
            self.flwers -= 1
        
    def add_flwing(self):
        self.flwings += 1

    def del_flwing(self):
        assert(self.flwings >= 0)
        if self.flwings > 0:
            self.flwings -= 1

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posters")
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.poster.username}"

    def add_likes(self):
        self.likes += 1

    def unlike(self):
        assert(self.likes >= 0)
        if self.likes > 0:
            self.likes -= 1

class Follower(models.Model):
    idol = models.ForeignKey(User, on_delete=models.CASCADE, related_name="idols")
    fan = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fans")

    class Meta:
        unique_together = ('idol', 'fan')

    def __str__(self):
        return f"{self.idol.username} <= {self.fan.username}"
    
class Like(models.Model):
    liking = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likings")
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likers")

    class Meta:
        unique_together = ('liking', 'liker')

    def __str__(self):
        return f"{self.liker.username} liked {self.liking.poster.username}'s post"

    