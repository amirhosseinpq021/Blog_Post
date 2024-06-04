from django.urls import path
from . import views


urlpatterns = [
    # posts crud by manager
    path('posts/', views.posts, name='my_dashboard')
    ]
