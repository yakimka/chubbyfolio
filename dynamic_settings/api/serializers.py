from rest_framework import serializers

from dynamic_settings.models import MainScreenPhoto


class FilterSettingsSerializer(serializers.Serializer):
    section = serializers.CharField(max_length=256, required=False)


class MainScreenPhotoSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%b %d, %Y')
    image_p1 = serializers.SerializerMethodField()
    image_p2 = serializers.SerializerMethodField()
    image_p3 = serializers.SerializerMethodField()
    image_p4 = serializers.SerializerMethodField()
    image_p5 = serializers.SerializerMethodField()
    image_p6 = serializers.SerializerMethodField()
    image_p7 = serializers.SerializerMethodField()

    class Meta:
        model = MainScreenPhoto
        fields = ['name', 'image_p1', 'image_p2', 'image_p3', 'image_p4',
                  'image_p5', 'image_p6', 'image_p7', 'date', 'priority']

    def _get_absolute_url(self, image):
        request = self.context.get('request')
        return request.build_absolute_uri(image.url)

    def get_image_p1(self, photo):
        return self._get_absolute_url(photo.image['p1'])

    def get_image_p2(self, photo):
        return self._get_absolute_url(photo.image['p2'])

    def get_image_p3(self, photo):
        return self._get_absolute_url(photo.image['p3'])

    def get_image_p4(self, photo):
        return self._get_absolute_url(photo.image['p4'])

    def get_image_p5(self, photo):
        return self._get_absolute_url(photo.image['p5'])

    def get_image_p6(self, photo):
        return self._get_absolute_url(photo.image['p6'])

    def get_image_p7(self, photo):
        return self._get_absolute_url(photo.image['p7'])
