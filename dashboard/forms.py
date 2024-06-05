from django import forms
from blog.models import Post


class BlogPostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'photo', 'short_description', 'blog_body')

