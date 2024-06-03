from django.urls import path
from . import views
from .views import HomeView, PostDetail, EditPost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', views.add_post, name='new_post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # delete and edit posts crud
    path('post/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

    # post_by_category
    path('<int:category_id>/',  views.posts_by_category, name='posts_by_category'),

]
