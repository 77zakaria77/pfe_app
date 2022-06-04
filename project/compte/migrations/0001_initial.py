# Generated by Django 4.0.4 on 2022-05-19 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoEcole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerant', models.CharField(blank=True, max_length=100, null=True)),
                ('wilaya', models.CharField(blank=True, max_length=100, null=True)),
                ('adresse', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin', models.IntegerField(verbose_name="Numéro de carte d'Identitée Nationale")),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('adresse', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adresse')),
                ('code_postal', models.IntegerField(blank=True, null=True)),
                ('wilaya', models.CharField(default='Alger', max_length=50)),
                ('commune', models.CharField(default='Sidi Mhamed', max_length=100)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('Group_sanguin', models.CharField(default='A+', max_length=3)),
                ('auto_école', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compte.autoecole')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriePermi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=2, null=True)),
                ('discription', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CentreExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('adresse', models.CharField(blank=True, max_length=200, null=True)),
                ('wilaya', models.CharField(default='Alger', max_length=50)),
                ('commune', models.CharField(default='Sidi Mhamed', max_length=100)),
                ('nbrPlace', models.IntegerField(blank=True, null=True)),
                ('statut', models.CharField(blank=True, max_length=50, null=True)),
                ('Numéro_agrément', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dnsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('heureDebut', models.TimeField(blank=True, null=True)),
                ('heureFin', models.TimeField(blank=True, null=True)),
                ('candidat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='compte.candidat')),
                ('centre_examen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compte.centreexamen')),
            ],
        ),
        migrations.CreateModel(
            name='Examinateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('wilaya', models.CharField(blank=True, max_length=200, null=True)),
                ('centre_examen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='compte.centreexamen')),
            ],
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('Code', 'Code'), ('Manoeuvre', 'Manoeuvre'), ('Conduite', 'Conduite')], default='Code', max_length=100)),
                ('résultat', models.CharField(blank=True, choices=[('Reçu', 'Reçu'), ('Echoué', 'Echoué')], max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('candidat', models.ManyToManyField(to='compte.candidat')),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='compte.session')),
            ],
        ),
        migrations.CreateModel(
            name='Dwsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('wilaya', models.CharField(blank=True, max_length=100, null=True)),
                ('dnsr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compte.dnsr')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidat',
            name='categorie_du_permis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='compte.categoriepermi'),
        ),
        migrations.AddField(
            model_name='candidat',
            name='dwsr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compte.dwsr'),
        ),
        migrations.AddField(
            model_name='candidat',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='autoecole',
            name='dwsr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compte.dwsr'),
        ),
    ]