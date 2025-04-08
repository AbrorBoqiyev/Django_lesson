from django.http import HttpResponse
from django.shortcuts import render
from .models import Countries

# Create your views here.
def orm_list(request):
    html = """ 
        <h1>working...</h1>
    """ 
    return HttpResponse(html)


def checker(request):
    context = {
        "title": 'Hello world',
        "text": 'This is my project',
    }
    return render(request, "index.html", context)