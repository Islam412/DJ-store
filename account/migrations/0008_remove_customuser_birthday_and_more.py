# Generated by Django 4.2 on 2023-08-12 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_customuser_age_remove_customuser_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='birthday_dayofyear_internal',
        ),
    ]
