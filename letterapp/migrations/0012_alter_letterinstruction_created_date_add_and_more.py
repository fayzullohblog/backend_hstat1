# Generated by Django 4.0 on 2023-12-15 07:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0011_alter_letterinstruction_created_date_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 7, 2, 16, 395838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 7, 2, 16, 396740, tzinfo=utc)),
        ),
    ]
