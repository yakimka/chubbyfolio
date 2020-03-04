import pytest
from django.core.exceptions import ValidationError

from photosets.models import upload_previews_to


@pytest.mark.parametrize('filename,expected', [
    ('image.jpg', 'uploads/main_screen/slider/image.jpg'),
    ('pic.JPEG', 'uploads/main_screen/slider/pic.JPEG'),
    ('file', 'uploads/main_screen/slider/file'),
])
def test_upload_previews_to(filename, expected):
    assert upload_previews_to(None, filename) == expected


def test_str(factory):
    photo = factory.photo()

    assert 'image.jpg' == str(photo)


@pytest.mark.parametrize('crop,expected', [
    ('', True),
    ('0,7', '0,7'),
    ('65,65', '65,65'),
])
def test_get_crop(factory, crop, expected):
    photo = factory.photo(crop=crop)

    assert expected == photo.get_crop()


def test_thumbnail(factory, settings):
    settings.PHOTOSET_PHOTO_WIDTH = 100
    settings.PHOTOSET_PHOTO_HEIGHT = 50
    settings.PHOTOSET_PHOTO_QUALITY = 95
    photo = factory.photo()

    thumb_options = photo.thumbnail.thumbnail_options
    assert (100, 50) == thumb_options['size']
    assert 95 == thumb_options['quality']
    assert True is thumb_options['crop']


@pytest.mark.parametrize('crop', [
    'd5,10',
    '1, 1',
    '11',
    '5,d10',
    '1a,10',
    '1,10f',
])
def test_clean_bad_crop(factory, crop):
    photo = factory.photo(crop=crop)

    with pytest.raises(ValidationError, match='Неверный формат поля "crop"'):
        photo.clean()


@pytest.mark.parametrize('crop', [
    '',
    'smart',
    '1,1',
    '0,0',
    '30,40',
])
def test_clean(factory, crop):
    photo = factory.photo(crop=crop)

    try:
        photo.clean()
    except ValidationError:
        pytest.fail('Unexpected ValidationError')
