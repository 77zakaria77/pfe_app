# Generated by Django 4.0.4 on 2022-05-29 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0018_alter_candidat_date_de_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='date_de_dossier',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 12, 31, 56, 872283)),
        ),
    ]
