# Generated by Django 2.2.5 on 2019-09-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photosets', '0003_remove_photo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='crop',
            field=models.CharField(blank=True, max_length=56),
        ),
    ]
