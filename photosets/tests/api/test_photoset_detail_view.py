from functools import partial

from rest_framework.reverse import reverse

url_func = partial(reverse, 'photoset_detail')


def test_view(factory, api):
    photoset = factory.photoset(published=True, create_photos=1)

    got = api.get(url_func([photoset.id]))

    assert photoset.name == got['name']
    assert photoset.description == got['description']


def test_not_published(factory, api):
    photoset = factory.photoset(published=False, create_photos=1)

    api.get(url_func([photoset.id]), expected_status_code=404)
