# Generated by Django 4.2 on 2023-08-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0050_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_items',
        ),
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.cartitem'),
        ),
    ]
