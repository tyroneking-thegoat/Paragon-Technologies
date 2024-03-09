from django.db import models
from django.core.validators import FileExtensionValidator

class PDFFile(models.Model):
    pdf_document = models.ForeignKey('PDFDocument', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return self.title
    
class PDFDocument(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title