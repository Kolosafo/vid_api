from pyexpat import model
from rest_framework import serializers
from .models import video_data

class VideoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = video_data
        fields = ['video_url', 'cover_photo_url', 'title']