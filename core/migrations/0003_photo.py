# Generated by Django 4.2.7 on 2023-12-03 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cart_buyer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tools')),
            ],
        ),
    ]