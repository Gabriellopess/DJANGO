# Generated by Django 2.2.4 on 2019-08-07 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_auto_20190807_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='comentarios',
            name='texto',
        ),
    ]