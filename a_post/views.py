from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required



def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'a_post/blog_home.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.filter(post=post)
    commentform = CommentForm()
    
    context = {
        'post': post,
        'commentform': commentform,
        'slug': slug,
        'comment': comment,
        }
    return render(request, 'a_post/post_detail.html', context)

@login_required
def comment_sent(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('post-detail', slug=slug)
    


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'a_post/category.html', {'category': category})