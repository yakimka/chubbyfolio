from rest_framework import serializers

from photosets.models import Photoset, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'name', 'description', 'image',
                  'date_created', 'date_updated')


class PhotosetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photoset
        fields = ('id', 'name', 'description', 'preview', 'show_on_mainpage',
                  'published', 'date_created', 'date_updated')


class FilterPhotosetsSerializer(serializers.Serializer):
    show_on_mainpage = serializers.NullBooleanField(required=False)
