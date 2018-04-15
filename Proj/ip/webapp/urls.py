"""ip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name ='index'),

    path('signup/',views.register_render ,name = 'register'),

    path('accounts/login/',views.login_render ,name = 'login_render'),
    path('sigin/authenticate/',views.loginreq ,name = 'loginreq'),

    path('newpost/',views.creates ,name = 'creates'),
    
    path('ideas/',views.ideas ,name = 'ideas'),
    path('ideas/<int:pk>/',views.viewIdeas ,name = 'viewIdeas'),
    path('ideas/<int:pk>/like',views.likePost ,name = 'like'),
    path('ideas/<int:pk>/comment',views.commentPost ,name = 'comment'),

    path('logout/',views.logoutrender ,name = 'logoutrender'),

    # path('',views. ,name = ''),
    # path('',views. ,name = ''),
]
