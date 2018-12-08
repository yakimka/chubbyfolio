from rest_framework import serializers

from photosets.models import Photoset, Photo


class PhotoSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField()

    class Meta:
        model = Photo
        fields = ('id', 'name', 'description', 'image', 'thumbnail',
                  'date_created', 'date_updated')


class PhotosetSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField()

    class Meta:
        model = Photoset
        fields = ('id', 'name', 'description', 'cover', 'preview', 'show_on_mainpage',
                  'published', 'date_created', 'date_updated')


class FilterPhotosetsSerializer(serializers.Serializer):
    show_on_mainpage = serializers.NullBooleanField(required=False)
