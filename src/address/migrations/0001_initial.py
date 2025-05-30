# Generated by Django 5.2 on 2025-05-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=64)),
                ("destrict", models.CharField(max_length=64)),
                ("region", models.CharField(max_length=64)),
                ("postal_code", models.CharField(blank=True, max_length=64, null=True)),
                ("country", models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
