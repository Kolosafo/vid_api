# Generated by Django 4.0 on 2022-02-23 05:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_video_data_user_id_alter_video_data_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unique_id',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video_data',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 23, 5, 24, 25, 699581, tzinfo=utc)),
        ),
    ]