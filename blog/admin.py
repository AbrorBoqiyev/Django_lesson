from django.contrib import admin
from .models import Author, Genre, Post

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Post)
