from django.shortcuts import render, redirect
from blog.models import Post


# Create your views here.


# posts crud by manager
from dashboard.forms import BlogPostsForm


def posts(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'dashboard/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        form = BlogPostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # temporarily saving the form
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = BlogPostsForm()
    context = {
        'form': form,
    }
    return render(request, 'new_post.html', context)

