from django.urls import path

from dynamic_settings.api.views import SettingsView

urlpatterns = [
    path('', SettingsView.as_view(), name='dynamic_settings_list'),
]
