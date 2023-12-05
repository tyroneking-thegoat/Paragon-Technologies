from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('signin', views.signin, name = "signin"),
    path('signup', views.signup, name = "signup"),
    path('signout', views.signout, name = "signout"),
    path('activate/<uidb64>/<token>', views.activate, name = "activate"),
    path('courses', views.courses, name = "courses"),
    path('CSCE1030', views.csce1030, name = "csce1030"),
    path('CSCE2100', views.csce2100, name = "csce2100"),
    path('CSCE3600', views.csce3600, name = "csce3600"),
]
