from django.db import models

class TestModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/",blank=True)
    
    def __str__(self):
        return self.title