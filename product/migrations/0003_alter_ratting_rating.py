# Generated by Django 4.2.3 on 2023-10-03 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_ratting_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratting',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
