# Generated by Django 4.0.4 on 2022-05-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0020_alter_other_info_position2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_info',
            name='signature',
            field=models.ImageField(default='No photo', null=True, upload_to='signature/', verbose_name='signature'),
        ),
    ]
