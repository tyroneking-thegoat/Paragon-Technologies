from django.urls import path
from . import views

app_name = "Course"

urlpatterns = [
    path('', views.home, name = "home"),
    path('courses', views.courses, name = "courses"),
    path('courses/csce1030', views.csce1030, name = "csce1030"),
    path('courses/csce2100', views.csce2100, name = "csce2100"),
    path('courses/csce3600', views.csce3600, name = "csce3600"),
]
