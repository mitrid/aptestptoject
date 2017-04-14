from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    """docstring for Post"""
    id
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(
            blank=True, null=True)
    author = models.ForeignKey('auth.User')


    def publish(self):
        self.created_at = timezone.now()
        self.save()
