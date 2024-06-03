from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'photo', 'short_description', 'blog_body']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'short_description', 'blog_body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


