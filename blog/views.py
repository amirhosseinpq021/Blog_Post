from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Post
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
