from django.db import models
from django.contrib.auth.models import User


class Count(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="count")

    def __str__(self):
        return f"{self.user.username} == {self.count} ==> {self.date}"
