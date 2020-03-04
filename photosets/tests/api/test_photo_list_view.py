from functools import partial

import pytest
from rest_framework.reverse import reverse

url_func = partial(reverse, 'photoset_photos')


@pytest.mark.parametrize('count', [
    0,
    3,
    5,
])
def test_view(factory, api, count):
    photoset = factory.photoset(published=True, create_photos=count)

    got = api.get(url_func([photoset.id]))

    assert count == got['count']
