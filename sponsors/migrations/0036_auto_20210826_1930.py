# Generated by Django 2.0.13 on 2021-08-26 19:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0035_auto_20210826_1929"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sponsorship",
            options={"permissions": [("sponsor_publisher", "Can access sponsor placement API")]},
        ),
    ]
