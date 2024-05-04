from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    photo = models.ImageField(upload_to='Images')
    Craeted_at = models.DateTimeField(auto_now_add=True)
