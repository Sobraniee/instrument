# Generated by Django 4.2.7 on 2023-11-28 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_category_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
