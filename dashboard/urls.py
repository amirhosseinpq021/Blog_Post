from django.urls import path
from . import views


urlpatterns = [
    # posts crud by manager
    path('posts/', views.posts, name='my_dashboard'),
    path('posts/add/', views.add_post, name='add_post_by_manager'),
    path('posts/edit/<int:pk>/', views.edit_post_by_manager, name='edit_post_by_manager'),
    path('posts/delete/<int:pk>/', views.delete_post_by_manager, name='delete_post_by_manager'),

    # comments crud by manager
    path('comments/', views.comments, name='comments'),

    path('comments/delete/<int:pk>/', views.delete_comments_by_manager, name='delete_comments_by_manager'),

]
