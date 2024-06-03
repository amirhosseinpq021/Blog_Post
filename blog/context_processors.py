from .models import Post, Category


def recent_post(request):
    recent_posts = Post.objects.order_by('-created_at')[:6]
    return dict(recent_posts=recent_posts)


def all_category(request):
    categories = Category.objects.all()
    return dict(categories=categories)
