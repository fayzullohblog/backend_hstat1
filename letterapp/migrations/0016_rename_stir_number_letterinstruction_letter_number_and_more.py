# Generated by Django 4.0 on 2023-12-28 06:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0015_remove_letterinstruction_litter_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letterinstruction',
            old_name='stir_number',
            new_name='letter_number',
        ),
        migrations.AddField(
            model_name='letterinstruction',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 6, 54, 36, 701263, tzinfo=utc)),
        ),
    ]
