# Generated by Django 4.2.7 on 2023-11-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_category_sub_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_name',
            field=models.JSONField(blank=True, null=True, verbose_name=models.CharField(max_length=255)),
        ),
    ]