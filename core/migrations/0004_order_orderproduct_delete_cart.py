# Generated by Django 5.0 on 2023-12-20 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_tools_photos_tools_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_order", models.PositiveIntegerField(unique=True)),
                ("buyer_name", models.CharField(max_length=255)),
                ("buyer_phone", models.CharField(max_length=15)),
                ("delivery", models.BooleanField()),
                ("delivery_address", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
        migrations.CreateModel(
            name="OrderProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="core.order",
                    ),
                ),
                (
                    "tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.tools"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт заказа",
                "verbose_name_plural": "Продукты заказа",
            },
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]