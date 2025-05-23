from django.http import HttpResponse
# from django.shortcuts import render
from .models import Post, Author
from django.db.models import Q
from django.db.models import Max


def blog_list(request):
    # posts = Post.objects.filter(Q(author__name__contains="malik")|Q(title__startswith='a'))
    # q1 = (Post.objects.filter(title__startswith='a'))
    # q2 = (Post.objects.filter(title__endswith='o'))
    # posts = q1.union(q2)
    # posts = Post.objects.filter(id__gt=1 , id__lt=4)
    # posts = Post.objects.only('title', 'publish')
    # posts = Post.objects.all()[1:3]
    # posts = Post.objects.all().order_by('-publish')  #DESC
    posts = Post.objects.all()
    # posts = Post.objects.all().order_by('-publish')
    # print(posts.query)
    article = Post.objects.select_related('author').get(id=2)
    readdress = Author.objects.get(id=4)
    print(readdress)
    print(article.author.name)
    
    # --------------------
    # CREATE
    # e = Post.objects.create(
    #     title='Evrica', content="bunday buyruq borligini ko'pchilik ehtimol bolmaydi bilmaganlar uchun yangili albatta evrica bo'ladi",
    # )
    # e.save()
    # --------------------
    # UPDATE
    # e = Post.objects.get(id=6)
    # e.title="Today's Evricas"
    # e.save()
    # --------------------
    # DELETE
    # e = Post.objects.get(id=5).delete()
    post_list = ""
    for post in posts:
        post_list += f"<li><strong>{post}</strong> | <I>{post.publish}</I>   </br> {post.content}</li>"
    return HttpResponse(f"<ol>{post_list}</ol> <br> {article.author.name}  <br>  {readdress} ")



