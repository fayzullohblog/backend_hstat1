# Generated by Django 4.2 on 2024-02-28 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lettersummonapp', '0019_alter_lettersummons_created_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 4, 4, 42, 39, 800983, tzinfo=datetime.timezone.utc)),
        ),
    ]