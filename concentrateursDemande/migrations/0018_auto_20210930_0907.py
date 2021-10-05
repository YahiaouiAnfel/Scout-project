# Generated by Django 2.2.24 on 2021-09-30 07:07

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0017_auto_20210930_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='numeroTel',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True, verbose_name='رقم هاتف مرافق المريض'),
        ),
    ]