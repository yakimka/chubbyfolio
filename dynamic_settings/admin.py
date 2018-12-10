from django.contrib import admin

from dynamic_settings.models import MainScreenPhoto


@admin.register(MainScreenPhoto)
class MainScreenPhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'date')
    list_editable = ('priority',)
    ordering = ('priority', 'date',)
