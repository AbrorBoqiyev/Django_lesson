from django.http import HttpResponse
from django.shortcuts import render


def blog_list(request):
    html = """
        <h1>Blog</h1>
    """
    return HttpResponse(html)