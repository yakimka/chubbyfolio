from rest_framework import generics

from feedback.api.serializers import MessageSerializer


class CreateMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    throttle_scope = 'message'
