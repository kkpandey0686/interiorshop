# Generated by Django 3.2 on 2021-04-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wholesale',
            field=models.BooleanField(default=False),
        ),
    ]
