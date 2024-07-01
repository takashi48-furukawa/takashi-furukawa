# Generated by Django 4.1 on 2024-06-14 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("TaskApp", "0004_merge_20240614_2023"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]