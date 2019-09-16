import re
from contextlib import suppress

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer


def upload_photosets_to(instance, filename):
    return 'uploads/photosets/{0}/{1}'.format(instance.photoset.id, filename)


def upload_previews_to(instance, filename):
    return 'uploads/main_screen/slider/{1}'.format(instance.id, filename)


def validate_photoset_photo(image):
    width = image.width
    height = image.height
    min_width = settings.PHOTOSET_PHOTO_WIDTH
    min_height = settings.PHOTOSET_PHOTO_HEIGHT
    if width < min_width or height < min_height:
        raise ValidationError(f'Минимальные размеры изображения: {min_width}x{min_height} пикселей')


class Photoset(models.Model):
    name = models.CharField(max_length=1024, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))
    preview = ThumbnailerImageField(upload_to=upload_previews_to,
                                    verbose_name=_('Превью для главной'),
                                    null=True, blank=True)
    show_on_mainpage = models.BooleanField(default=False, verbose_name=_('Показывать на главной'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Фотосет')
        verbose_name_plural = _('Фотосеты')
        ordering = ['-date_created']

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
        cover = self.photos.filter(is_cover=True).first()
        if not cover:
            cover = self.photos.last()

        return cover.thumbnail if cover else None

    @property
    def preview_thumbnail(self):
        with suppress(InvalidImageFormatError):
            return self.preview['home_slider']
        return self.preview


class Photo(models.Model):
    image = ThumbnailerImageField(upload_to=upload_photosets_to,
                                  verbose_name=_('Изображение'),
                                  validators=[validate_photoset_photo])
    photoset = models.ForeignKey(Photoset, related_name='photos', null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Фотосет'))
    crop = models.CharField(max_length=56, blank=True)
    is_cover = models.BooleanField(default=False, verbose_name=_('Обложка'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Фото')
        verbose_name_plural = _('Фото')
        ordering = ['-date_created']

    def __str__(self):
        return self.image.url.split('/')[-1]

    def get_crop(self):
        return True if self.crop == '' else self.crop

    @property
    def thumbnail(self):
        width = settings.PHOTOSET_PHOTO_WIDTH
        height = settings.PHOTOSET_PHOTO_HEIGHT
        quality = settings.PHOTOSET_PHOTO_QUALITY
        options = {'size': (width, height), 'crop': self.get_crop(), 'quality': quality}

        thumb = get_thumbnailer(self.image).get_thumbnail(options)
        return thumb

    def clean(self):
        regexp = r'^-?\d+,-?\d+$'
        if self.crop not in ['', 'smart'] and not re.search(regexp, self.crop):
            raise ValidationError(_('Неверный формат поля "crop"'))
        super().clean()
