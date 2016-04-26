from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    author = models.ForeignKey(User)
    
    posted = models.DateTimeField(default=now)
    
    tags = models.ManyToManyField(Tag, related_name="posts")
    
    def display_tags(self):
        return ', '.join([a.name for a in self.tags.all()])
    
    def __str__(self):
        return self.title;
    
    