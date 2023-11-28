# Generated by Django 4.2.6 on 2023-11-22 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0003_letterinstruction_created_date_add_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lettersummons',
            name='inn_number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lettersummons',
            name='state',
            field=models.BooleanField(choices=[(True, 'Topshirdi'), (False, 'Topshirmadi')], default=False),
        ),
        migrations.AlterField(
            model_name='letterinstruction',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 10, 24, 41, 402385, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 10, 24, 41, 402857, tzinfo=datetime.timezone.utc)),
        ),
    ]