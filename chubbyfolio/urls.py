from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from photosets.api.views import PhotosetViewSet

router = SimpleRouter()
router.register(r'photosets', PhotosetViewSet, basename='photoset')

urlpatterns = [
    path('flf7eiu2ocn/', admin.site.urls),
    path('api/', include([
        path('', include(router.urls), name='photosets'),
        path('dynamic-settings/', include('dynamic_settings.urls'), name='dynamic_settings'),
        path('feedback/', include('feedback.urls'), name='feedback'),
    ]), name='api')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
