# Generated by Django 4.0.1 on 2022-01-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0002_job_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_listing',
            name='salary',
            field=models.PositiveIntegerField(verbose_name='salary'),
        ),
    ]
