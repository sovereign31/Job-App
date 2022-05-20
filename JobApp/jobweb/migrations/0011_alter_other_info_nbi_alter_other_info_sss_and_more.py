# Generated by Django 4.0.4 on 2022-05-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobweb', '0010_alter_account_registration_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_info',
            name='NBI',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='NBI'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='SSS',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='SSS'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='TIN',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='TIN'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='company2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='company2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='from2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='from_2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='med_record',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='med_record'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='pagibig',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='pagibig'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='philhealth',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='philhealth'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='position2',
            field=models.CharField(blank=True, max_length=99, verbose_name='position2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='ref1',
            field=models.CharField(max_length=99, null=True, verbose_name='ref1'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='ref2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='ref2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refcom1',
            field=models.CharField(max_length=99, null=True, verbose_name='refcom1'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refcom2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='refcom2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refcon1',
            field=models.CharField(max_length=99, null=True, verbose_name='refcon1'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refcon2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='refcon2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refpos1',
            field=models.CharField(max_length=99, null=True, verbose_name='refpos1'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='refpos2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='refpos2'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='signature',
            field=models.ImageField(null=True, upload_to='', verbose_name='signature'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='to1',
            field=models.CharField(max_length=99, null=True, verbose_name='to_1'),
        ),
        migrations.AlterField(
            model_name='other_info',
            name='to2',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='to_2'),
        ),
    ]