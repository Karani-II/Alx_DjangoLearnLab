from django.db import models
from django.conf import settings
from accounts.models import CustomUser 
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='comments')

class Like(models.Model):
    User_Liking = models.ForeignKey(CustomUser,on_delete = models.CASCADE, related_name = 'User_liking')
    Post_liked = models.ForeignKey(Post, on_delete =models.CASCADE, related_name="Liked_post")
    class Meta:
        unique_together = ('User_Liking', 'Post_liked')


    


# Create your models here.
