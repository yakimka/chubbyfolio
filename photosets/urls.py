from django.urls import path

from photosets.api.views import PhotosetList, PhotosetDetail

urlpatterns = [
    path('', PhotosetList.as_view(), name='photosets'),
    path('<int:pk>/', PhotosetDetail.as_view(), name='photosets_detail'),
]
