from django.urls import path
from . import views

# /user
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout)
]