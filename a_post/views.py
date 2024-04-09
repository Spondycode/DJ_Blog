from django.shortcuts import render
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'a_post/blog_home.html', {'posts': posts})
