# Generated by Django 2.2.24 on 2021-10-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0023_demandetraite'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='NCI',
            field=models.CharField(default='', max_length=200, verbose_name='رقم بطاقة التعريف الوطنية'),
        ),
    ]