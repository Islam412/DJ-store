# Generated by Django 4.2 on 2023-07-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_wishlistitem_description_wishlistitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='wishlist_images/'),
        ),
    ]
