from django.http import HttpResponse
# from django.shortcuts import render
from .models import Post


def blog_list(request):
    posts = Post.objects.filter(title__endswith='o')
    print(posts.query)
    post_list = ""
    for post in posts:
        post_list += f"<li>{post} / {post.publish}</li>"
    return HttpResponse(f"<ul>{post_list}</ul>")



