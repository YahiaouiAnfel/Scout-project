# Generated by Django 2.2.24 on 2021-09-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrateursDemande', '0016_auto_20210930_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='autre',
            field=models.TextField(default='', verbose_name='ملاحظات أخرى'),
        ),
    ]
