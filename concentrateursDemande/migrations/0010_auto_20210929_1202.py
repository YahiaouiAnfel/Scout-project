# Generated by Django 2.2.24 on 2021-09-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0009_auto_20210929_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='nomPrenom',
            field=models.CharField(default='', max_length=200, verbose_name='Nom et prénom'),
        ),
    ]
