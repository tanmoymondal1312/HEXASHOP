# Generated by Django 4.2.3 on 2023-09-23 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_seller_created'),
        ('store', '0003_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_products', to='seller.seller'),
        ),
    ]
