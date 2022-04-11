from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logoutUser,name='logout'),
]
