# Generated by Django 4.2 on 2023-07-25 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_alter_wishlistitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='name',
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='product',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='wishlist',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='shop.wishlist'),
            preserve_default=False,
        ),
    ]
