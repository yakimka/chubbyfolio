from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from easy_thumbnails.fields import ThumbnailerImageField


def upload_photos_to(instance, filename):
    return 'uploads/main_screen/second_screen/{0}'.format(filename)


class MainScreenPhoto(models.Model):
    MAX_OBJECTS = 7

    name = models.CharField(max_length=40, verbose_name=_('подпись'))
    image = ThumbnailerImageField(upload_to=upload_photos_to, verbose_name=_('изображение'))
    date = models.DateField(verbose_name=_('дата съемки'))
    priority = models.IntegerField(unique=True,
                                   choices=[(i, i) for i in range(1, MAX_OBJECTS + 1)], null=True,
                                   blank=True, verbose_name=_('очередность'))

    class Meta:
        ordering = ['priority', 'date']
        verbose_name = _('фотография на главной')
        verbose_name_plural = _('фотографии на главной')

    def __str__(self):
        return self.name

    def clean(self):
        # Don't allow create more than n photos
        if self.pk is None and MainScreenPhoto.objects.count() >= self.MAX_OBJECTS:
            raise ValidationError(
                _('Разрешено максимум %(count)d фотографий' % {'count': self.MAX_OBJECTS}))
        super().clean()
