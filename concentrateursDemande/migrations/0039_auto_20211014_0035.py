# Generated by Django 2.2.24 on 2021-10-13 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0038_auto_20211014_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandetraite',
            name='dateRetour',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ إعادة المكثف'),
        ),
    ]