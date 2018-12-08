from rest_framework import generics

from photosets.api.serializers import PhotosetSerializer, FilterPhotosetsSerializer, \
    PhotoSerializer
from photosets.models import Photoset, Photo


class PhotosetList(generics.ListAPIView):
    # Select all published photosets
    # and photosets with at least one photo
    queryset = Photoset.objects.filter(published=True).exclude(photos=None)
    serializer_class = PhotosetSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        serializer = FilterPhotosetsSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        show_on_mainpage = serializer.data.get('show_on_mainpage')
        if show_on_mainpage is not None:
            queryset = queryset.filter(show_on_mainpage=show_on_mainpage)
        return queryset


class PhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Photo.objects.filter(photoset__pk=pk)


class PhotosetDetail(generics.RetrieveAPIView):
    queryset = Photoset.objects.filter(published=True)
    serializer_class = PhotosetSerializer
