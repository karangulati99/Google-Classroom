# Generated by Django 2.2.4 on 2019-09-23 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_coursename_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursename',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 23, 5, 7, 9, 976618)),
        ),
    ]
