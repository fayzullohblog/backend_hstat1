# Generated by Django 4.0 on 2024-01-08 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lettersummonapp', '0018_alter_lettersummons_created_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 13, 6, 14, 52, 928452, tzinfo=utc)),
        ),
    ]
