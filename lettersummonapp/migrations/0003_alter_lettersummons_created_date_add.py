# Generated by Django 4.0 on 2023-12-21 06:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lettersummonapp', '0002_alter_lettersummons_created_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 6, 40, 1, 359261, tzinfo=utc)),
        ),
    ]