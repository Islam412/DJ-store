# Generated by Django 4.2 on 2023-08-06 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.subcategory'),
        ),
    ]
