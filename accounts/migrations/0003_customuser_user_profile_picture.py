# Generated by Django 4.2.3 on 2023-09-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='photos/user_profile_picture'),
        ),
    ]
