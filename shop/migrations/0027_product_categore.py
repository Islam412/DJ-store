# Generated by Django 4.2 on 2023-07-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_remove_product_categore'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Categore',
            field=models.CharField(blank=True, choices=[('Laptop', 'Laptop'), ('Computer', 'Computer'), ('Phone', 'Phone'), ('Screen', 'Screen')], max_length=50, null=True),
        ),
    ]
