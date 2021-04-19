from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('addpost', views.add_post, name='add_post')
]
