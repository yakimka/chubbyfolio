from django.db import models
from django.utils.translation import gettext as _


def upload_to(instance, filename):
    return 'uploads/photosets/{0}/{1}'.format(instance.photoset.id, filename)


class Photoset(models.Model):
    class Meta:
        verbose_name = _('фотосет')
        verbose_name_plural = _('фотосеты')

    name = models.CharField(max_length=1024, verbose_name=_('название'))
    description = models.TextField(blank=True, verbose_name=_('описание'))
    published = models.BooleanField(default=True, verbose_name=_('опубликовано'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1} photos)'.format(self.name, self.photos.count())


class Photo(models.Model):
    name = models.CharField(max_length=1024, blank=True, verbose_name=_('название'))
    description = models.TextField(blank=True, verbose_name=_('описание'))
    image = models.ImageField(upload_to=upload_to, verbose_name=_('изображение'))
    photoset = models.ForeignKey(Photoset, related_name='photos', null=True,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('фотосет'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.image.url.split('/')[-1]
