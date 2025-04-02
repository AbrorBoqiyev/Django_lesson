from django.http import HttpResponse
# from django.shortcuts import render
from .models import Post
from django.db.models import Q


def blog_list(request):
    posts = Post.objects.filter(Q(author__name__contains="malik")|Q(title__startswith='a'))
    print(posts.query)
    post_list = ""
    for post in posts:
        post_list += f"<li><strong>{post}</strong> | <I>{post.publish}</I>  </br> {post.content}</li>"
    return HttpResponse(f"<ul>{post_list}</ul>")



