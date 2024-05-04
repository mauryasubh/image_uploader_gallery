from django.contrib import admin
from  .models import ImageUpload

# Register your models here.

class AdminImageUpload(admin.ModelAdmin):
    list_display = ['id', 'photo', 'Craeted_at']

admin.site.register(ImageUpload,AdminImageUpload)