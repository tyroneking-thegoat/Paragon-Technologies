from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "enrollment_codes"

urlpatterns = [
    path('', views.enroll, name = "enrollment_codes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
