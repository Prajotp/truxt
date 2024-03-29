# Generated by Django 5.0.2 on 2024-03-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_role"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="date_joined",),
        migrations.RemoveField(model_name="customuser", name="first_name",),
        migrations.RemoveField(model_name="customuser", name="is_active",),
        migrations.RemoveField(model_name="customuser", name="is_staff",),
        migrations.RemoveField(model_name="customuser", name="is_superuser",),
        migrations.RemoveField(model_name="customuser", name="last_login",),
        migrations.RemoveField(model_name="customuser", name="last_name",),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
