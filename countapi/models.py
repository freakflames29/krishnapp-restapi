from django.db import models
from django.contrib.auth.models import User


class Count(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField()
    time = models.CharField(max_length=100,default="00:00:00")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="count")

    def __str__(self):
        return f"{self.user.username} == {self.count} ==> {self.date}"
