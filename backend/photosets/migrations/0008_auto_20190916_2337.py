# Generated by Django 2.2.5 on 2019-09-16 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photosets', '0007_remove_photo_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoset',
            options={'ordering': ['-date_created'], 'verbose_name': 'Фотосет', 'verbose_name_plural': 'Фотосеты'},
        ),
    ]
