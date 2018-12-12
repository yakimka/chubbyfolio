import re
from rest_framework import serializers

from feedback.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('name', 'phone', 'email', 'text')

    def validate_phone(self, phone):
        return re.sub('[^0-9]', '', phone)
