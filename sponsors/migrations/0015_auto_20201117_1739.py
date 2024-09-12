# Generated by Django 2.0.13 on 2020-11-17 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sponsors", "0014_auto_20201116_1437"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsorship",
            name="submited_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="sponsorship",
            name="for_modified_package",
            field=models.BooleanField(
                default=False,
                help_text="If true, it means the user customized the package's benefits.",
            ),
        ),
    ]
