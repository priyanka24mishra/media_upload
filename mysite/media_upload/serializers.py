from django.apps import apps
from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from media_upload.models import MediaUpload


class MediaUploadSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = MediaUpload
        fields = ['name_song_podcast_audio', 'duration', 'uploaded_time', 'host','participants','title_of_audiobook','author_of_title','narrator','upload_type']
        read_only_fields = ['id']

    
    def validate(self, data):

        errors = {}

        if data['upload_type'] == 'song':

            if 'name_song_podcast_audio' not in data or not data['name_song_podcast_audio']:
                errors.update({'name_song_podcast_audio':'Name of the song is required'})


        if data['upload_type'] == 'podcast':

            if 'name_song_podcast_audio' not in data or not data['name_song_podcast_audio']:
                errors.update({'name_song_podcast_audio':'Name of the podcast is required'})

            if 'host' not in data or not data['host']:
                errors.update({'host':'Host name is required for podcast'})

        if data['upload_type'] == 'audiobook':

            if 'title_of_audiobook' not in data or not data['title_of_audiobook']:
                errors.update({'title_of_audiobook':'Title of audiobook is required for audiobook'})

            if 'author_of_title' not in data or not data['author_of_title']:
                errors.update({'author_of_title':'Author of the title is required for audiobook'})
            
            if 'narrator' not in data or not data['narrator']:
                errors.update({'narrator':'Author of the title is required for audiobook'})


        if errors:
            raise serializers.ValidationError(errors)
        return data