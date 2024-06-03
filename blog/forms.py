from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'photo', 'short_description', 'blog_body']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'short_description', 'blog_body']


