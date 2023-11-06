from django.urls import path
from . import views

app_name = "Course"

urlpatterns = [
    path('', views.home, name = "home")
]
