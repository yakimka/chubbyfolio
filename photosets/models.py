from contextlib import suppress
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.fields import ThumbnailerImageField


def upload_photosets_to(instance, filename):
    return 'uploads/photosets/{0}/{1}'.format(instance.photoset.id, filename)


def upload_previews_to(instance, filename):
    return 'uploads/main_screen/slider/{1}'.format(instance.id, filename)


class Photoset(models.Model):
    class Meta:
        verbose_name = _('фотосет')
        verbose_name_plural = _('фотосеты')

    name = models.CharField(max_length=1024, verbose_name=_('название'))
    description = models.TextField(blank=True, verbose_name=_('описание'))
    published = models.BooleanField(default=True, verbose_name=_('опубликовано'))
    preview = ThumbnailerImageField(upload_to=upload_previews_to, verbose_name=_('превью для главной'),
                                null=True, blank=True)
    show_on_mainpage = models.BooleanField(default=False, verbose_name=_('показывать на главной'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1} photos)'.format(self.name, self.photos.count())

    def clean(self):
        # Don't allow set show_on_mainpage to True
        # if model has not preview image
        if self.show_on_mainpage and not self.preview:
            raise ValidationError(_('Фотосет должен содержать "Превью для главной"'))
        super().clean()

    @property
    def cover(self):
        first_photo = self.photos.first()
        return first_photo.thumbnail if first_photo else None

    @property
    def preview_thumbnail(self):
        with suppress(InvalidImageFormatError):
            return self.preview['home_slider']
        return self.preview


class Photo(models.Model):
    name = models.CharField(max_length=1024, blank=True, verbose_name=_('название'))
    description = models.TextField(blank=True, verbose_name=_('описание'))
    image = ThumbnailerImageField(upload_to=upload_photosets_to, verbose_name=_('изображение'))
    photoset = models.ForeignKey(Photoset, related_name='photos', null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('фотосет'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.image.url.split('/')[-1]

    @property
    def thumbnail(self):
        with suppress(InvalidImageFormatError):
            return self.image['600x675c']
        return self.image
