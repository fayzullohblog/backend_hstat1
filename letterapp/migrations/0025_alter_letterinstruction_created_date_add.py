# Generated by Django 4.0 on 2024-01-08 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0024_letterinstruction_pdf_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 6, 14, 52, 927356, tzinfo=utc)),
        ),
    ]
