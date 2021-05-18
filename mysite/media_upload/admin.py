from django.contrib import admin

# Register your models here.
from django.contrib import admin
from media_upload.models import MediaUpload


admin.site.register(MediaUpload)
