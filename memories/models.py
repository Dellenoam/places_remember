from django.contrib.auth.models import User
from django.db import models


class Memories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=166)
    location = models.TextField()
