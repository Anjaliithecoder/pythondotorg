# Generated by Django 2.0.13 on 2021-08-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0039_auto_20210827_1248"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsorshippackage",
            name="logo_dimension",
            field=models.PositiveIntegerField(default=175),
        ),
        migrations.AlterField(
            model_name="sponsorship",
            name="level_name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="DEPRECATED: shall be removed after manual data sanity check.",
                max_length=64,
            ),
        ),
    ]
