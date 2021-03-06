# Generated by Django 4.0.4 on 2022-05-25 13:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0011_session_nom_alter_candidat_date_de_dossier'),
    ]

    operations = [
        migrations.AddField(
            model_name='epreuve',
            name='Examinateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='compte.examinateur'),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='date_de_dossier',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 25, 15, 7, 58, 581543)),
        ),
    ]
