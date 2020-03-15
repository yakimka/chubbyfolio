from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from photosets.api.serializers import (
    PhotosetSerializer, FilterPhotosetsSerializer, PhotoSerializer)
from photosets.models import Photoset, Photo


class PhotosetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Photoset.objects.filter(published=True).exclude(photos=None)
    serializer_class = PhotosetSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            serializer = FilterPhotosetsSerializer(data=self.request.query_params)
            serializer.is_valid(raise_exception=True)
            show_on_mainpage = serializer.data.get('show_on_mainpage')
            if show_on_mainpage is not None:
                queryset = queryset.filter(show_on_mainpage=show_on_mainpage)
        return queryset

    @action(detail=True)
    def photos(self, request, pk=None):
        photos = Photo.objects.filter(photoset__pk=pk)

        page = self.paginate_queryset(photos)
        if page is not None:
            serializer = PhotoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
