from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
