from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'a_post/blog_home.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'a_post/post_detail.html', {'post': post})

    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        
        if name and comment:
            Comment.objects.create(
                post=post, 
                name=name, 
                comment=comment
                )
            return redirect('post_detail', slug=slug)
        
    return render(request, 'a_post/post_detail.html', {'post': post})
