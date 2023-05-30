# Generated by Django 4.1 on 2023-05-29 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_alter_quiz_options_alter_useranswermap_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="option_1",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="option_2",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="option_3",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="option_4",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="userquizsession",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="answer",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="useranswermap",
            name="user_answer",
            field=models.CharField(max_length=256),
        ),
    ]