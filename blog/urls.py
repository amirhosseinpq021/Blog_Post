from django.urls import path

from .views import HomeView, NewPost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', NewPost.as_view(), name='new_post')
]
