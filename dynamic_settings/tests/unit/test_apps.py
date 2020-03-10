from django.apps import apps

from dynamic_settings.apps import DynamicSettingsConfig


def test_apps_config():
    assert DynamicSettingsConfig.name == 'dynamic_preferences'
    assert apps.get_app_config('dynamic_preferences').name == 'dynamic_preferences'
