import pytest
from rest_framework.reverse import reverse

URL = reverse('photoset-list')


def test_url():
    assert '/api/photosets/' == URL


@pytest.mark.parametrize('count', [
    0,
    3,
])
def test_view(factory, api, count):
    factory.cycle(count).photoset(published=True, create_photos=1)

    got = api.get(URL)

    assert count == got['count']


@pytest.mark.parametrize('count', [
    0,
    3,
])
def test_get_show_on_mainpage(factory, api, count):
    factory.cycle(2).photoset(published=True, create_photos=1)
    factory.cycle(count).photoset(published=True, create_photos=1, show_on_mainpage=True)

    got = api.get(URL, data={'show_on_mainpage': True})

    assert count == got['count']
    assert all([item['show_on_mainpage'] is True for item in got['results']])


@pytest.mark.parametrize('count', [
    0,
    3,
])
def test_get_show_on_mainpage_false(factory, api, count):
    factory.cycle(2).photoset(published=True, create_photos=1, show_on_mainpage=True)
    factory.cycle(count).photoset(published=True, create_photos=1)

    got = api.get(URL, data={'show_on_mainpage': False})

    assert count == got['count']
    assert all([item['show_on_mainpage'] is False for item in got['results']])
