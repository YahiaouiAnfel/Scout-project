# Generated by Django 2.2.24 on 2021-10-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0037_demandetraite_dateretour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandetraite',
            name='dateRetour',
            field=models.DateField(blank=True, verbose_name='تاريخ إعادة المكثف'),
        ),
    ]
