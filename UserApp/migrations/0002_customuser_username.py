# Generated by Django 4.1 on 2024-06-19 02:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("UserApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=150,
                unique=True,
                verbose_name="username",
            ),
            preserve_default=False,
        ),
    ]
