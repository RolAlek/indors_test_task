# Generated by Django 5.1.1 on 2024-10-06 04:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0004_remove_cat_years_cat_birth_year"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="cat",
            constraint=models.UniqueConstraint(
                fields=("name", "owner"), name="unique_name_owner"
            ),
        ),
    ]
