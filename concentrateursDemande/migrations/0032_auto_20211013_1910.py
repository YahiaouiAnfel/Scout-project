# Generated by Django 2.2.24 on 2021-10-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0031_auto_20211013_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandetraite',
            name='dateRetour',
            field=models.DateField(default='2021-10-13', verbose_name='تاريخ تسليم المكثف'),
        ),
    ]
