from django.urls import path

from .views import HomeView, NewPost, PostDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail')

]
