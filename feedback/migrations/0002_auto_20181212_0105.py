# Generated by Django 2.1.3 on 2018-12-11 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
    ]
