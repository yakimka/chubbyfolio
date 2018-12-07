# Generated by Django 2.1.3 on 2018-12-07 17:07

from django.db import migrations, models
import photosets.models


class Migration(migrations.Migration):

    dependencies = [
        ('photosets', '0002_auto_20181205_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoset',
            name='preview',
            field=models.ImageField(null=True, upload_to=photosets.models.upload_previews_to, verbose_name='превью для главной'),
        ),
        migrations.AddField(
            model_name='photoset',
            name='show_on_mainpage',
            field=models.BooleanField(default=False, verbose_name='показывать на главной'),
        ),
    ]
