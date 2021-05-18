from django.urls import path 
from media_upload.views import MediaUploadView, MediaUploadDetailView


urlpatterns = [
    path('', MediaUploadView.as_view()),
    path('<int:upload_type_id>/', MediaUploadDetailView.as_view())
]