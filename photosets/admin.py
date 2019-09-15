from django import forms
from django.conf import settings
from django.contrib import admin
from django.forms import models, widgets
from easy_thumbnails.files import get_thumbnailer

from .models import Photoset, Photo

THUMB_WIDTH = settings.PHOTOSET_PHOTO_WIDTH / 3
THUMB_HEIGHT = settings.PHOTOSET_PHOTO_HEIGHT / 3


class ThumbnailerImageWidget(forms.ClearableFileInput):
    template_name = 'admin/thubnailer_image_widget.html'

    def __init__(self, attrs=None, template=None, width=200, height=225):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if context['widget']['is_initial']:
            context['widget'].update({
                'preview_image': self._get_preview_image(value).url,
            })
        return context

    def _get_preview_image(self, image):
        width = 0 if image.width > image.height else self.width
        height = 0 if image.height > image.width else self.height
        options = {'size': (int(width), int(height)), 'crop': True, 'quality': 90}

        return get_thumbnailer(image).get_thumbnail(options)


class PhotoAdminForm(models.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'image', 'crop')

        widgets = {
            'crop': widgets.HiddenInput(attrs={'class': 'image-crop'}),
            'image': ThumbnailerImageWidget(width=THUMB_WIDTH, height=THUMB_HEIGHT)
        }


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
    form = PhotoAdminForm
    fields = ('name', 'image', 'crop')


@admin.register(Photoset)
class PhotosetAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('id', 'name', 'published', 'show_on_mainpage', 'date_created')
    list_display_links = ('id', 'name')
    list_editable = ('published', 'show_on_mainpage',)
    ordering = ('date_created',)

    class Media:
        js = ('js/admin/jquery.Jcrop.min.js', 'js/admin/photosets.js')
        css = {'all': ('css/admin/jquery.Jcrop.css',)}

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)
