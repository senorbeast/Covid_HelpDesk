from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('addpost', views.add_post, name='add_post'),
    path('rhelp', views.add_rhelp, name='rhelp'),
    path('fbform', views.fbform, name='fbform')
]
