from rest_framework import generics

from photosets.api.serializers import PhotosetSerializer
from photosets.models import Photoset


class PhotosetList(generics.ListAPIView):
    queryset = Photoset.objects.filter(published=True)
    serializer_class = PhotosetSerializer


class PhotosetDetail(generics.RetrieveAPIView):
    queryset = Photoset.objects.filter(published=True)
    serializer_class = PhotosetSerializer
