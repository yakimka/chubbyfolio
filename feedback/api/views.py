from rest_framework import viewsets, mixins

from feedback.api.serializers import MessageSerializer


class MessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = MessageSerializer
