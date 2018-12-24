import re
from rest_framework import serializers

from feedback.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('name', 'phone', 'email', 'text')

    def validate_phone(self, phone):
        phone = re.sub('[^0-9]', '', phone)
        if len(phone) != 12:
            raise serializers.ValidationError("Номер телефона должен состоять из 12 цифр")
        return re.sub('[^0-9]', '', phone)
