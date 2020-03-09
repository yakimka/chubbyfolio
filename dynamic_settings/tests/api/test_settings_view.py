import pytest
from dynamic_preferences.registries import global_preferences_registry
from rest_framework.reverse import reverse

URL = reverse('dynamic_settings_list')


@pytest.fixture
def global_preferences():
    global_preferences = global_preferences_registry.manager()
    global_preferences['social__instagram_link'] = 'https://instagram.com/test'
    global_preferences['social__facebook_link'] = 'https://facebook.com/test'
    global_preferences['social__phone_number'] = '380631234567'

    return global_preferences


def test_settings_list(factory, global_preferences, api):
    ms_photo = factory.main_screen_photo(priority=2)

    got = api.get(URL)
    got_photo = got['main_screen_photos'][0]

    assert 2 == got_photo['priority']
    assert ms_photo.name == got_photo['name']
    assert '460x657' in got_photo['image']
    assert {
               'instagram_link': 'https://instagram.com/test',
               'facebook_link': 'https://facebook.com/test',
               'phone_number': '380631234567'
           } == got['social']


def test_settings_list_select_section_social(factory, global_preferences, api):
    factory.main_screen_photo()

    got = api.get(URL, data={'section': 'social'})

    assert {
               'instagram_link': 'https://instagram.com/test',
               'facebook_link': 'https://facebook.com/test',
               'phone_number': '380631234567'
           } == got


def test_settings_list_select_section_(factory, global_preferences, api):
    factory.main_screen_photo()

    got = api.get(URL, data={'section': 'main_screen_photos'})

    assert '460x657' in got[0]['image']
