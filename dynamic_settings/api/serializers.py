from contextlib import suppress
from django.utils import dateformat
from easy_thumbnails.exceptions import InvalidImageFormatError
from rest_framework import serializers

from dynamic_settings.models import MainScreenPhoto


class FilterSettingsSerializer(serializers.Serializer):
    section = serializers.CharField(max_length=256, required=False)


class MainScreenPhotoSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = MainScreenPhoto
        fields = ['name', 'image', 'date', 'priority']

    def _get_absolute_url(self, image):
        request = self.context.get('request')
        return request.build_absolute_uri(image.url)

    def get_date(self, photo):
        return dateformat.format(photo.date, 'F d, Y')

    def get_image(self, photo):
        photos = self.context.get('photos')
        order_number = next(i for i, j in enumerate(photos) if j.pk == photo.pk)
        with suppress(InvalidImageFormatError):
            return self._get_absolute_url(photo.image['p{0}'.format(order_number + 1)])
        return ''
