from django.db import models
# -*- Coding: utf-8 -*-
from django.template import Context, Template
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

