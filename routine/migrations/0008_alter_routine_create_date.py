# Generated by Django 3.2.5 on 2021-12-22 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0007_alter_routine_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 22, 18, 12, 49, 325534)),
        ),
    ]
