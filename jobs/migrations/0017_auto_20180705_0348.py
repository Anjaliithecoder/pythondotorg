# Generated by Django 2.0.6 on 2018-07-05 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0016_auto_20170821_2000"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="category",
            field=models.ForeignKey(
                limit_choices_to={"active": True},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jobs",
                to="jobs.JobCategory",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_types",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"active": True},
                related_name="jobs",
                to="jobs.JobType",
                verbose_name="Job technologies",
            ),
        ),
    ]
