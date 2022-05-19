# Generated by Django 3.2.5 on 2022-04-28 10:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220428_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_created_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 10, 38, 25, 208372, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 10, 38, 25, 208372, tzinfo=utc)),
        ),
    ]
