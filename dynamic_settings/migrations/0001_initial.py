# Generated by Django 2.1.3 on 2018-12-10 18:58

from django.db import migrations, models
import dynamic_settings.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainScreenPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='подпись')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=dynamic_settings.models.upload_photos_to, verbose_name='изображение')),
                ('date', models.DateField(verbose_name='дата съемки')),
            ],
        ),
    ]
