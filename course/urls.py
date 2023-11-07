from django.urls import path
from . import views

app_name = "Course"

urlpatterns = [
    path('', views.home, name = "home"),
    path('courses', views.courses, name = "courses"),
    path('courses/CSCE1030', views.csce1030, name = "csce1030"),
    path('courses/CSCE2100', views.csce2100, name = "csce2100"),
    path('courses/CSCE3600', views.csce3600, name = "csce3600"),
]
