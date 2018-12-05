from django.contrib import admin

from .models import Photoset, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


@admin.register(Photoset)
class PhotosetAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)
