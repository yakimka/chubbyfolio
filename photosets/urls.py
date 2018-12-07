from django.urls import path

from photosets.api.views import PhotosetList, PhotosetDetail, PhotoList

urlpatterns = [
    path('', PhotosetList.as_view(), name='photosets'),
    path('<int:pk>/', PhotosetDetail.as_view(), name='photoset_detail'),
    path('<int:pk>/photos/', PhotoList.as_view(), name='photoset_photos'),
]
