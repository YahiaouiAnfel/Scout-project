# Generated by Django 2.2.24 on 2021-10-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0030_auto_20211006_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandetraite',
            name='date',
        ),
        migrations.AddField(
            model_name='demandetraite',
            name='dateEnvoie',
            field=models.DateField(default='2021-10-13', verbose_name='تاريخ تسليم المكثف'),
        ),
        migrations.AddField(
            model_name='demandetraite',
            name='dateRetour',
            field=models.DateField(default='2021-10-13', verbose_name='تاريخ تسليم المكثف'),
        ),
        migrations.AlterField(
            model_name='demande',
            name='dateDemande',
            field=models.DateField(default='2021-10-13', verbose_name='تاريخ تسليم المكثف'),
        ),
    ]