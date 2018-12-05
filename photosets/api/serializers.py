from rest_framework import serializers

from photosets.models import Photoset, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'name', 'description', 'image',
                  'date_created', 'date_updated')


class PhotosetSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    date_created = serializers.DateTimeField()

    class Meta:
        model = Photoset
        fields = ('id', 'name', 'description', 'published', 'photos',
                  'date_created', 'date_updated')
