from dynamic_preferences.registries import global_preferences_registry
from rest_framework.response import Response
from rest_framework.views import APIView

from dynamic_settings.api.serializers import FilterSettingsSerializer


class SettingsView(APIView):

    def get(self, request):
        global_preferences = global_preferences_registry.manager()
        social_prefs = global_preferences.queryset.filter(
            section='social').extra(  # just for experience
            select={'link': 'raw_value'}
        ).values('name', 'link')
        self.data = {
            'social': {pref['name']: pref['link'] for pref in social_prefs}
        }

        return Response(self.filter_settings())

    def filter_settings(self):
        serializer = FilterSettingsSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        section = serializer.data.get('section')
        if section and section in self.data:
            self.data = self.data.get(section)
        return self.data
