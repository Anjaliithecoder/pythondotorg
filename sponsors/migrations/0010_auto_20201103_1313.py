# Generated by Django 2.0.13 on 2020-11-03 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0009_auto_20201103_1259"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sponsorship",
            name="sponsor_info",
        ),
        migrations.AddField(
            model_name="sponsor",
            name="description",
            field=models.TextField(
                default="",
                help_text="Brief description of the sponsor for public display.",
                verbose_name="Sponsor description",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sponsor",
            name="landing_page_url",
            field=models.URLField(
                blank=True,
                help_text="Sponsor landing page URL. This may be provided by the sponsor, however the linked page may not contain any sales or marketing information.",
                null=True,
                verbose_name="Sponsor landing page",
            ),
        ),
        migrations.AddField(
            model_name="sponsor",
            name="mailing_address",
            field=models.TextField(default="", verbose_name="Sponsor Mailing/Billing Address"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sponsor",
            name="name",
            field=models.CharField(
                default="",
                help_text="Name of the sponsor, for public display.",
                max_length=100,
                verbose_name="Sponsor name",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sponsor",
            name="primary_phone",
            field=models.CharField(default="", max_length=32, verbose_name="Sponsor Primary Phone"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sponsor",
            name="print_logo",
            field=models.FileField(
                blank=True,
                help_text="For printed materials, signage, and projection. SVG or EPS",
                null=True,
                upload_to="sponsor_print_logos",
                verbose_name="Sponsor print logo",
            ),
        ),
        migrations.AddField(
            model_name="sponsor",
            name="web_logo",
            field=models.ImageField(
                default="",
                help_text="For display on our sponsor webpage. High resolution PNG or JPG, smallest dimension no less than 256px",
                upload_to="sponsor_web_logos",
                verbose_name="Sponsor web logo",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sponsorship",
            name="sponsor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.Sponsor",
            ),
        ),
        migrations.DeleteModel(
            name="SponsorInformation",
        ),
    ]
