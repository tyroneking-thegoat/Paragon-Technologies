from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('signin', views.signin, name = "signin"),
    path('signup', views.signup, name = "signup"),
    path('signout', views.signout, name = "signout"),
    path('activate/<uidb64>/<token>', views.activate, name = "activate"),
    path('courses', views.courses, name = "courses")
]
