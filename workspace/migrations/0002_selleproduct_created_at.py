# Generated by Django 4.2.3 on 2023-10-10 03:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 12, 0)),
        ),
    ]
