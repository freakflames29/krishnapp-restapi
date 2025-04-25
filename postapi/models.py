from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="post/",blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    

