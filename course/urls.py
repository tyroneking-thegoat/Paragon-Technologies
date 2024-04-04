from django.urls import path
from . import views
from .views import view_pdf
from django.conf import settings
from django.conf.urls.static import static


app_name = "Course"

urlpatterns = [
    #path('', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    #path('courses/<str:folder>/<str:filename>/', views.view_pdf, name="view_pdf"),  # URL pattern for view_pdf
    path('courses/CSCE1030', views.csce1030, name="csce1030"),
    path('courses/CSCE2100', views.csce2100, name="csce2100"),
    path('courses/CSCE3600', views.csce3600, name="csce3600"),
    path('pdfs/<int:pdf_id>/', view_pdf, name='view_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
