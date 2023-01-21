# Generated by Django 4.1.5 on 2023-01-21 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accountability_app", "0002_tag_alter_post_post_text_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 21, 8, 40, 20, 213503, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date published",
            ),
        ),
    ]