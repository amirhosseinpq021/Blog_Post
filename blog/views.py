from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Post, Category
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class NewPost(CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'


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

