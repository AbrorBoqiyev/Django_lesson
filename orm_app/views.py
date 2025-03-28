from django.http import HttpResponse
from django.shortcuts import render
from .models import Countries

# Create your views here.
def orm_list(request):
    countries = Countries.objects.all()
    country_list = ""
    for c in countries:
        country_list += f"<li>{c}</li>"   
    return HttpResponse(f"<ul>{country_list}</ul>")