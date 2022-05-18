# Generated by Django 4.0.1 on 2022-05-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0002_remove_account_registration_password1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_registration',
            name='password1',
            field=models.CharField(default='', max_length=20, verbose_name='password1'),
        ),
        migrations.AlterField(
            model_name='account_registration',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
