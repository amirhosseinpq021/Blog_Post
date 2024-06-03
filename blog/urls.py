from django.urls import path

from .views import HomeView, NewPost, PostDetail, EditPost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # delete and edit posts crud
    path('post/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

]
