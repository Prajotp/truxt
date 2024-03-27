# Generated by Django 5.0.2 on 2024-03-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_remove_customuser_role_id_customuser_role_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="role_name",),
        migrations.AddField(
            model_name="customuser",
            name="role_id",
            field=models.IntegerField(default=None, null=True),
        ),
    ]