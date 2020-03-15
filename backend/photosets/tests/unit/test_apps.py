from django.apps import apps

from photosets.apps import PhotosetsConfig


def test_apps_config():
    assert PhotosetsConfig.name == 'photosets'
    assert apps.get_app_config('photosets').name == 'photosets'
