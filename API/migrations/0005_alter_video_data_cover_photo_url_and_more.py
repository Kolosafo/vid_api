# Generated by Django 4.0 on 2022-02-09 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_video_data_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_data',
            name='cover_photo_url',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='video_data',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 10, 57, 27, 510481, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='video_data',
            name='video_desc',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='video_data',
            name='video_url',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
