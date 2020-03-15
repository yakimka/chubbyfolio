import io

import pytest
from django.core.exceptions import ValidationError

from photosets.models import upload_photosets_to, validate_photoset_photo


@pytest.mark.parametrize('id,filename,expected', [
    (23, 'image.jpg', 'uploads/photosets/23/image.jpg'),
    ('32', 'pic.JPEG', 'uploads/photosets/32/pic.JPEG'),
    ('slug', 'file', 'uploads/photosets/slug/file'),
])
def test_upload_photosets_to(mocker, id, filename, expected):
    instance = mocker.MagicMock()
    instance.photoset.id = id

    assert upload_photosets_to(instance, filename) == expected


@pytest.mark.parametrize('width,height', [
    (200, 160),
    (400, 100),
    (100, 100),
])
def test_validate_photoset_photo_error(settings, mocker, width, height):
    settings.PHOTOSET_PHOTO_WIDTH = 300
    settings.PHOTOSET_PHOTO_HEIGHT = 150
    image = mocker.MagicMock(width=width, height=height)

    with pytest.raises(ValidationError, match='Минимальные размеры изображения: 300x150 пикселей'):
        validate_photoset_photo(image)


@pytest.mark.parametrize('width,height', [
    (301, 151),
    (400, 400),
])
def test_validate_photoset_photo(settings, mocker, width, height):
    settings.PHOTOSET_PHOTO_WIDTH = 300
    settings.PHOTOSET_PHOTO_HEIGHT = 150
    image = mocker.MagicMock(width=width, height=height)

    assert validate_photoset_photo(image) is None


@pytest.mark.parametrize('photos', [
    0, 1, 2, 3, 4, 5
])
def test_str(factory, photos):
    photoset = factory.photoset(create_photos=photos)

    assert f'{photoset.name} ({photos} photos)' == str(photoset)


@pytest.mark.parametrize('is_show_on_mainpage,is_preview', [
    (False, True),
    (False, False),
    (True, True),
])
def test_clean(factory, is_show_on_mainpage, is_preview):
    photoset = factory.photoset(show_on_mainpage=is_show_on_mainpage, create_preview=is_preview)
    try:
        photoset.clean()
    except ValidationError:
        pytest.fail('Unexpected ValidationError')


def test_clean_error(factory):
    photoset = factory.photoset(show_on_mainpage=True, create_preview=False)

    with pytest.raises(ValidationError, match='Фотосет должен содержать "Превью для главной"'):
        photoset.clean()


def test_cover_empty(factory):
    photoset = factory.photoset()

    assert photoset.cover is None


def test_cover_auto(factory):
    photoset = factory.photoset(create_photos=3)

    assert photoset.cover == photoset.photos.last().thumbnail


def test_cover_manual(factory):
    photoset = factory.photoset(create_photos=3)
    photo = photoset.photos.all()[1]
    photo.is_cover = True
    photo.save()

    assert photoset.cover == photo.thumbnail


def test_preview_thumbnail(factory):
    photoset = factory.photoset(create_preview=True)

    assert photoset.preview_thumbnail == photoset.preview['home_slider']


def test_preview_thumbnail_invalid_format(factory):
    photoset = factory.photoset(create_preview=True, preview=io.BytesIO())

    assert photoset.preview_thumbnail == photoset.preview
