# Generated by Django 4.1 on 2024-06-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserApp", "0006_alter_customuser_groups_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="email",
        ),
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                default="default_username",
                max_length=150,
                unique=True,
                verbose_name="username",
            ),
        ),
    ]
