# Generated by Django 3.2.5 on 2021-12-22 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_auto_20211214_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 22, 18, 12, 49, 324533)),
        ),
    ]
