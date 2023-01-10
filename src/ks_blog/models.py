from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

POST_STATUS = (
    ('d', "DRAFT"),
    ('p', "PUBLISHED"),
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField()
    status = models.CharField(max_length=2, choices=POST_STATUS)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = HTMLField()