# Generated by Django 4.1 on 2023-05-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0005_alter_useranswermap_user_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="userquizsession",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]