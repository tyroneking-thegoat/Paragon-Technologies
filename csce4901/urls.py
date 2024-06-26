"""
URL configuration for csce4901 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from enrollment_codes import views
from django.conf import settings
from django.conf.urls.static import static
# from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth.urls')),
    #path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('course/', include('course.urls')),
    path('upload/', include('upload.urls')),
    path("account/", include("account.urls")),
    path('enroll/', views.enroll, name='enrollment_codes'),
    path('check-enrollment', views.check_enrollment, name='check_enrollment'),
    path('create-class/', views.create_class, name='create_class'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)