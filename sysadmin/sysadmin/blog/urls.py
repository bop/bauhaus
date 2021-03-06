from django.conf.urls import *
# -*- coding:Utf-8 -*-
from django.views.generic import ListView, DetailView
from sysadmin.blog.models import Post

urlpatterns = patterns('sysadmin.blog.views',
                       url(r'^$', ListView.as_view(
            queryset=Post.objects.all().order_by("-created"),
            template_name="blog/blog2.html")),

                       url(r'^(?P<pk>\d*)$', DetailView.as_view(
            model = Post,
            template_name="blog/post.html")),

                       url(r'^archives$', ListView.as_view(
            queryset=Post.objects.all().order_by("-created"),
            template_name="blog/archives.html")),

                       url(r'^tag/(?P<tag>\w*)$', 'tagpage'),
            

)

