# Generated by Django 4.0 on 2022-02-09 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_remove_video_data_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_data',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 10, 51, 36, 765031, tzinfo=utc)),
        ),
    ]
