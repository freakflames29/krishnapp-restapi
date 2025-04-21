from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="post/",blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    
    def __str__(self):
        return self.title
    
    

