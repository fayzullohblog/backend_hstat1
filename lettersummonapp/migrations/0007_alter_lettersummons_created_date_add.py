# Generated by Django 4.0 on 2023-12-25 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lettersummonapp', '0006_alter_lettersummons_created_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 11, 4, 43, 850800, tzinfo=utc)),
        ),
    ]
