# Generated by Django 4.0 on 2023-12-27 13:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0008_letterinstruction_typeletter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 26, 13, 1, 30, 941434, tzinfo=utc)),
        ),
    ]
