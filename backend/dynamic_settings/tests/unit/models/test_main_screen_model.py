import pytest
from django.core.exceptions import ValidationError


def test_str(factory):
    ms_photo = factory.main_screen_photo()

    assert ms_photo.name == str(ms_photo)


@pytest.mark.parametrize('count', [
    7, 8, 15
])
def test_clean_error(factory, count):
    ms_photos = factory.cycle(count).main_screen_photo()
    new = ms_photos[0]
    new.pk = None

    with pytest.raises(ValidationError, match='Разрешено максимум 7 фотографий'):
        new.clean()


@pytest.mark.parametrize('count', [
    1, 5, 6
])
def test_clean(factory, count):
    ms_photos = factory.cycle(count).main_screen_photo()
    new = ms_photos[0]
    new.pk = None

    try:
        new.clean()
    except ValidationError:
        pytest.raises('Unexpected ValidationError')
