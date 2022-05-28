# Generated by Django 4.0.4 on 2022-05-28 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0025_other_info_verified_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='other_info',
            name='verified_user',
        ),
        migrations.AddField(
            model_name='account_registration',
            name='verified_user',
            field=models.BooleanField(default=False, max_length=99, verbose_name='verified_user'),
        ),
    ]