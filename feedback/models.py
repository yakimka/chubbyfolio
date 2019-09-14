from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=25)
    text = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return '{0} | {1}'.format(self.name, self.phone)
