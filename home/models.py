from django.db import models

# Create your models here.
class Thumbnail(models.Model):
    title=models.CharField(max_length=150)
    # slug=models.SlugField(unique=True) # no idea what that does
    img=models.FileField(upload_to="pic/%y/", default='placeholderPreview.jpg')

    def __str__(self):
        return self.title
    class Meta :
        ordering=('-id',)