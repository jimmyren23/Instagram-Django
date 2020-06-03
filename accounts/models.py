from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = 1)
    date_created = models.DateTimeField(auto_now_add = True)
    post_pic = models.ImageField(null = True, blank = True)
    liked = models.ManyToManyField(User, default = None, blank = True, related_name = 'liked')
    
    @property 
    def num_likes(self):
        return self.liked.all().count()
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    value = models.CharField(choices = LIKE_CHOICES,default = 'Like', max_length = 10)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)