# Generated by Django 5.1.1 on 2024-10-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0002_cat_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cat",
            name="birth_date",
        ),
        migrations.AddField(
            model_name="cat",
            name="years",
            field=models.IntegerField(default=1, verbose_name="Возраст"),
            preserve_default=False,
        ),
    ]
