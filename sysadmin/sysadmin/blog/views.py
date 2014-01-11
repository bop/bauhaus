from sysadmin.blog.models import Post
# -*- coding:Utf-8 -*-
from django.shortcuts import render_to_response
from django.template import loader, Context

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("blog/tagpage.html", {"posts":posts, "tag":tag})
