# Generated by Django 4.0.1 on 2022-04-28 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0010_alter_account_registration_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_registration',
            name='employment_status',
            field=models.CharField(default='Not yet Employed', max_length=99, verbose_name='job'),
        ),
    ]