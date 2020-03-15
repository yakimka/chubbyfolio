import io

import pytest
from django.utils import dateformat

from dynamic_settings.api.serializers import MainScreenPhotoSerializer
from dynamic_settings.models import MainScreenPhoto


def test_get_date(factory):
    ms_photo = factory.main_screen_photo()

    serializer = MainScreenPhotoSerializer(ms_photo)

    assert dateformat.format(ms_photo.date, 'F d, Y') == serializer.get_date(ms_photo)


@pytest.fixture
def ms_photos(factory):
    return factory.cycle(7).main_screen_photo()


@pytest.fixture
def context(rf):
    request = rf.get('/api/dynamic-settings/')
    context = {
        'photos': list(MainScreenPhoto.objects.all()),
        'request': request
    }

    return context


@pytest.mark.parametrize('image_num,size', [
    # size from settings THUMBNAIL_ALIASES
    (1, '460x657'),
    (2, '558x585'),
    (3, '967x657'),
    (4, '560x557'),
    (5, '460x657'),
    (6, '326x469'),
    (7, '360x531'),
])
def test_get_image(factory, ms_photos, context, image_num, size):
    ms_photo = MainScreenPhoto.objects.all()[image_num - 1]
    serializer = MainScreenPhotoSerializer(ms_photo, context=context)

    url = serializer.get_image(ms_photo)

    assert size in url


@pytest.fixture
def ms_photos_invalid_image(factory):
    return factory.cycle(7).main_screen_photo(image=io.BytesIO())


def test_get_image_invalid_format(factory, ms_photos_invalid_image, context):
    ms_photo = MainScreenPhoto.objects.all()[0]
    serializer = MainScreenPhotoSerializer(ms_photo, context=context)

    url = serializer.get_image(ms_photo)

    assert '' == url
