# Generated by Django 3.0.4 on 2020-04-19 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
