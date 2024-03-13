# Generated by Django 5.0.2 on 2024-03-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_discount_price_alter_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='User',
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7),
        ),
    ]
