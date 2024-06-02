from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView
from .models import Post
from .forms import PostForm
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
