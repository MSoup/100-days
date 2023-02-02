# Generated by Django 4.1.5 on 2023-02-02 01:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accountability_app", "0004_alter_post_pub_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["id"]},
        ),
        migrations.RenameField(
            model_name="post",
            old_name="post_text",
            new_name="text",
        ),
        migrations.RemoveField(
            model_name="post",
            name="pub_date",
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="date published",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="accountability_app.tag"),
        ),
    ]
