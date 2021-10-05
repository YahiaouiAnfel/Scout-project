# Generated by Django 2.2.24 on 2021-10-02 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0022_auto_20211001_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeTraite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاريخ تسليم المكثف')),
                ('concentrateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concentrateursDemande.Concentrateur')),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concentrateursDemande.Demande')),
            ],
        ),
    ]