# Generated by Django 4.0.2 on 2022-02-26 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_remove_profile_first_name_remove_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dateofbirth',
            field=models.DateField(default=datetime.datetime(2022, 2, 26, 10, 8, 49, 356698), null=True),
        ),
    ]