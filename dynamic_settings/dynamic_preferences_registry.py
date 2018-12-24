from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

# we create some section objects to link related preferences together
social = Section('social')


# We start with a global preference
@global_preferences_registry.register
class InstagramLink(StringPreference):
    section = social
    name = 'instagram_link'
    verbose_name = 'Instagram link'
    default = ''
    required = False


@global_preferences_registry.register
class FacebookLink(StringPreference):
    section = social
    name = 'facebook_link'
    verbose_name = 'Facebook link'
    default = ''
    required = False
