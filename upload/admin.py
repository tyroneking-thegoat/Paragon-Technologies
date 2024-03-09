from django.contrib import admin
from .models import PDFDocument, PDFFile

admin.site.register(PDFDocument)
admin.site.register(PDFFile)