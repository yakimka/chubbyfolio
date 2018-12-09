from rest_framework import serializers


class FilterSettingsSerializer(serializers.Serializer):
    section = serializers.CharField(max_length=256, required=False)
