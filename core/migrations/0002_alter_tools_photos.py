# Generated by Django 4.2.4 on 2023-12-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tools",
            name="photos",
            field=models.ImageField(upload_to="tools_photos"),
        ),
    ]