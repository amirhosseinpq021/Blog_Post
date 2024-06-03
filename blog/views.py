from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Post, Category, Comment
from .forms import PostForm, EditPostForm, CommentForm, EditCommentForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


# class NewPost(CreateView):
#     model = Post
#     template_name = 'new_post.html'
#     form_class = PostForm
#     success_url = reverse_lazy('home')


@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # temporarily saving the form
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'new_post.html', context)


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     context_object_name = 'post_detail'


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditPostForm


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    context_object_name = 'delete'


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Post.objects.filter(category=category_id).order_by('-created_at')
    # Use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     #     # redirect the user to homepage
    #     return redirect('home')

    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)


@login_required(login_url='login')
def detail_post(request, pk):
    single_blog = get_object_or_404(Post, pk=pk)
    # comments
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = single_blog
            comment.save()
            return HttpResponseRedirect(request.path_info)

    else:
        comment_form = CommentForm()
        comment = Comment.objects.filter(blog=single_blog)

    context = {
        'post_detail': single_blog,
        'comments': comment,
        'comment_form': comment_form,
    }
    return render(request, 'post_detail.html', context)


def search(request):
    keyword = request.GET.get('keyword')

    blog_search = Post.objects.filter(
        Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))

    context = {
        'blogs': blog_search,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)


# edit and delete
def edit_comment(request, pk):
    comments = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comments)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditCommentForm(instance=comments)

    context = {

        'form': form,
        'comments': comments,

    }
    return render(request, 'edit_comment.html', context)


def delete_comment(request, pk):
    comments = get_object_or_404(Comment, pk=pk)
    comments.delete()
    return redirect('home')

