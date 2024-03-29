# Generated by Django 2.2.5 on 2019-09-16 19:25

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import photosets.models


class Migration(migrations.Migration):

    dependencies = [
        ('photosets', '0004_photo_crop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-date_created'], 'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='photoset',
            options={'ordering': ['-date_updated'], 'verbose_name': 'Фотосет', 'verbose_name_plural': 'Фотосеты'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=photosets.models.upload_photosets_to, validators=[photosets.models.validate_photoset_photo], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photoset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photosets.Photoset', verbose_name='Фотосет'),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='preview',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=photosets.models.upload_previews_to, verbose_name='Превью для главной'),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='show_on_mainpage',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной'),
        ),
    ]
