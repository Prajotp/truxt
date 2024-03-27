# Generated by Django 5.0.2 on 2024-03-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_remove_customuser_role_name_customuser_role_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="account_id",),
        migrations.RemoveField(model_name="customuser", name="role_id",),
        migrations.AddField(
            model_name="customuser",
            name="role_name",
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]