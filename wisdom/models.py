from django.db import models

class Wisdom(models.Model):
    wisdom = models.TextField()
    
    
    def __str__(self):
        return self.wisdom