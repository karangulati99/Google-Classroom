# Generated by Django 2.2.4 on 2019-09-23 05:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190923_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursename',
            name='updated',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]