# Create your views here.
from media_upload.models import MediaUpload
from media_upload.serializers import MediaUploadSerializer
from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from media_upload.decorators import validate_media_file
from django.db import transaction


class MediaUploadView(generics.GenericAPIView):
    serializer_class = MediaUploadSerializer

    @transaction.atomic
    def post(self, request, upload_type):    
        data = request.data  
        data['upload_type'] = upload_type  
        serializer = MediaUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Media upoaded successfully", 'status_code': status.HTTP_200_OK})
        return Response(data=serializer.errors)

    
    def get(self, request, upload_type):
        if upload_type == 'song':
            uploaded_data = MediaUpload.objects.filter(upload_type = upload_type).values('id','name_song_podcast_audio','duration','uploaded_time')
        if upload_type == 'podcast':
            uploaded_data = MediaUpload.objects.filter(upload_type = upload_type).values('id','name_song_podcast_audio','duration','uploaded_time','host','participants')
        if upload_type == 'audiobook':
            uploaded_data = MediaUpload.objects.filter(upload_type = upload_type).values('id','title_of_audiobook','author_of_title','narrator','duration','uploaded_time')
        return Response({'message':'Data retrieved successfully','status_code': status.HTTP_200_OK, 'data':uploaded_data})

class MediaUploadDetailView(generics.GenericAPIView):

    def get(self, request, upload_type, upload_type_id):

        if upload_type == 'song':
            uploaded_data = MediaUpload.objects.filter(upload_type = upload_type, id=upload_type_id).values('id','name_song_podcast_audio','duration','uploaded_time')
        if upload_type == 'podcast':
            uploaded_data = MediaUpload.objects.filter(upload_type = upload_type, id=upload_type_id).values('id','name_song_podcast_audio','duration','uploaded_time','host','participants')
        if upload_type == 'audiobook':
            uploaded_data = MediaUpload.objects.filter(upload_type = upload_type, id=upload_type_id).values('id','title_of_audiobook','author_of_title','narrator','duration','uploaded_time')
        return Response({'status_code': status.HTTP_200_OK, 'data':uploaded_data})

    @validate_media_file
    @transaction.atomic   
    def put(self, request,upload_type, upload_type_id):
        data = request.data  
        data['upload_type'] = upload_type 
        media_instance = MediaUpload.objects.get(id=upload_type_id, upload_type=upload_type)
        serializer = MediaUploadSerializer(media_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Media updated successfully", 'status_code': status.HTTP_200_OK})
        return Response(data=serializer.errors)


    @validate_media_file
    @transaction.atomic   
    def delete(self, request, upload_type, upload_type_id):
        media_data = MediaUpload.objects.get(id=upload_type_id, upload_type=upload_type)
        media_data.delete()
        return Response({'message': "Media deleted successfully", 'status_code': status.HTTP_200_OK})