from decimal import Decimal
from django.contrib.postgres.fields import CICharField
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class MediaUpload(models.Model):
    UPLOAD_TYPE_CHOICES = [
        ('song', 'Song'),
        ('podcast', 'Podcast'),
        ('audiobook', 'Audiobook')
    ]

    name_song_podcast_audio = models.CharField(max_length=100, blank=True)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    participants = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True, blank=True, size=10)
    title_of_audiobook = models.CharField(max_length=100, blank=True, null=True)
    author_of_title = models.CharField(max_length=100, blank=True, null=True)
    narrator = models.CharField(max_length=100, blank=True, null=True)
    upload_type = models.CharField(max_length=30, choices=UPLOAD_TYPE_CHOICES, default=None, blank=False, null=False)

    class Meta:
        db_table = 'media_uploads'

    def __str__(self):
        return self.name_song_podcast_audio
