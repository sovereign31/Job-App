# Generated by Django 4.0.4 on 2022-05-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0013_alter_account_registration_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_info',
            name='signature',
            field=models.ImageField(default='', null=True, upload_to='signature/', verbose_name='signature'),
        ),
    ]
