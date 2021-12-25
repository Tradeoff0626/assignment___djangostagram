"""djangostagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from post.views import post_list, post_write

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('dsuser.urls')),
    path('post/', include('post.urls')),
    path('upload/', post_write),						# 게시물 작성 바로 연결
    path('', post_list)											# 게시물 목록 바로 연결
]
