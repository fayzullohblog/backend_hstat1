# Generated by Django 4.0 on 2023-12-28 07:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0020_rename_letter_number_letterinstruction_litter_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 7, 36, 57, 824271, tzinfo=utc)),
        ),
    ]
