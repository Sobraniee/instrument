# Generated by Django 4.2.7 on 2023-12-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_tools_photos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='tools',
            name='photos',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
