# Generated by Django 4.2.7 on 2023-11-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='photos',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]