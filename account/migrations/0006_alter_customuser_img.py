# Generated by Django 4.2 on 2023-08-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_customuser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.ImageField(blank=True, default='profile_images/default_profile.jpeg', null=True, upload_to='profile_images/'),
        ),
    ]
