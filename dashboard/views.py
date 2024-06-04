from django.shortcuts import render
from blog.models import Post


# Create your views here.


# posts crud by manager

def posts(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'dashboard/posts.html', context)
