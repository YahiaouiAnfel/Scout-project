# Generated by Django 2.2.24 on 2021-10-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0036_auto_20211013_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandetraite',
            name='dateRetour',
            field=models.DateField(default='2021-10-13', verbose_name='تاريخ إعادة المكثف'),
        ),
    ]