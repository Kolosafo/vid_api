# Generated by Django 4.0 on 2022-02-09 11:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_alter_video_data_cover_photo_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video_data',
            old_name='video_desc',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='video_data',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 11, 9, 17, 545796, tzinfo=utc)),
        ),
    ]
