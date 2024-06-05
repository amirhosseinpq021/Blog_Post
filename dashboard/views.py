from django.shortcuts import render, redirect
from blog.models import Post, Comment


from django.shortcuts import get_object_or_404

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


def edit_post_by_manager(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = BlogPostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_dashboard')

    else:
        form = BlogPostsForm(instance=post)
    context = {
        'form': form,
        'post': post,
        }
    return render(request, 'dashboard/edit_posts.html', context)


def delete_post_by_manager(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('my_dashboard')

# _____________________________________________________________________________________________________________________


def comments(request):
    all_comment = Comment.objects.all()
    context = {
        'all_comment': all_comment,
    }
    return render(request, 'dashboard/all_comments.html', context)





