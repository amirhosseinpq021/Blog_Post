from django.urls import path
from . import views
from .views import HomeView, EditPost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', views.add_post, name='new_post'),
    path('post/<int:pk>/', views.detail_post, name='post_detail'),

    # delete and edit posts crud
    path('post/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

    # post_by_category
    path('<int:category_id>/',  views.posts_by_category, name='posts_by_category'),

    # edit and delete comments by
    path('edit/<int:pk>/', views.edit_comment, name='edit_comments'),
    path('delete/<int:pk>/', views.delete_comment, name='delete_comments'),

]


