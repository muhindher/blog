from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from post import views


urlpatterns = [

    path('index',views.index,name="index"),
    path('addpost',views.AddPost, name="add_post"),
    path('',views.home,name='home'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('detail/<int:pk>',views.Detailpost,name='Detail_post'),
]
