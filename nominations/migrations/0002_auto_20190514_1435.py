# Generated by Django 2.0.13 on 2019-05-14 14:35

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("nominations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="election",
            name="_description_rendered",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="election",
            name="description",
            field=markupfield.fields.MarkupField(null=True, rendered_field=True),
        ),
        migrations.AddField(
            model_name="election",
            name="description_markup_type",
            field=models.CharField(
                choices=[
                    ("", "--"),
                    ("html", "HTML"),
                    ("plain", "Plain"),
                    ("markdown", "Markdown"),
                    ("restructuredtext", "Restructured Text"),
                ],
                default="markdown",
                editable=False,
                max_length=30,
            ),
        ),
    ]
