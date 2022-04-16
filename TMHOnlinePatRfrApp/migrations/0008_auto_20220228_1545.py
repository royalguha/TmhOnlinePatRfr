# Generated by Django 3.2 on 2022-02-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMHOnlinePatRfrApp', '0007_referral_details_payer_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral_details',
            name='cancel_remarks',
            field=models.TextField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='referral_details',
            name='is_cancel',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='referral_details',
            name='doc_ph',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Referred by Phone'),
        ),
        migrations.AlterField(
            model_name='referral_details',
            name='ip_no',
            field=models.CharField(max_length=120, null=True, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='referral_details',
            name='patient_type',
            field=models.CharField(choices=[('', 'Click to Select'), ('Cash', 'Cash'), ('Insurance', 'Insurance'), ('Corporate', 'Corporate')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='referral_details',
            name='payer_details',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
