from django.shortcuts import render, get_object_or_404
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'a_post/blog_home.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'a_post/post_detail.html', {'post': post})


