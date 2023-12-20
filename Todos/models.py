from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, default="Enter your title")
    description = models.TextField(null=True)
    created_at = models.DateTimeField("Created", default=datetime.now())

    updated_at = models.DateTimeField("Updated", default=datetime.now())


def __str__(self):
    return self.title
