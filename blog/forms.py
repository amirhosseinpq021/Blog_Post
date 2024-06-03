from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'short_description', 'blog_body']


