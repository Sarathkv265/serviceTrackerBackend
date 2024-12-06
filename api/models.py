from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    title=models.CharField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices=(("pending", "pending"), ("completed", "completed"))
    status=models.CharField(max_length=100, choices=status_choices, default="pending")
    created_date=models.DateTimeField(auto_now=True)
