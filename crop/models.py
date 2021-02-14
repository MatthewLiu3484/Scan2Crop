from __future__ import unicode_literals
	
from django.db import models
import uuid

# Create your models here.



class Post(models.Model):
    name = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True)
    image = models.ImageField(null = True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)