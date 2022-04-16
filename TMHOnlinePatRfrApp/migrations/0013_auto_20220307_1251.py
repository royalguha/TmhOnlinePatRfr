# Generated by Django 3.2 on 2022-03-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMHOnlinePatRfrApp', '0012_auto_20220307_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral_details',
            name='admission_time',
            field=models.TimeField(null=True, verbose_name='Admission Time'),
        ),
        migrations.AddField(
            model_name='referral_details',
            name='discharge_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Discharge Date/Time'),
        ),
        migrations.AddField(
            model_name='referral_details',
            name='patient_current_status',
            field=models.CharField(blank=True, choices=[('', 'A'), ('', 'B'), ('', 'C'), ('', 'D')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='referral_details',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='referral_details',
            name='speciality',
            field=models.CharField(default='', max_length=100),
        ),
    ]