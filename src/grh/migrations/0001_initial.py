# Generated by Django 3.2.15 on 2024-11-27 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255, null=True)),
                ('code', models.CharField(max_length=25, null=True, unique=True)),
                ('lien', models.CharField(max_length=255, null=True)),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('statut', models.CharField(choices=[('VALIDE', 'Valide'), ('SUPPRIME', 'Supprime'), ('BROUILLON', 'Brouillon'), ('CLOTURE', 'Cloture')], default='VALIDE', max_length=15, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('formulegarantie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.formulegarantie')),
                ('police', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.police')),
            ],
            options={
                'verbose_name': 'Campagne',
                'verbose_name_plural': 'campagnes',
                'db_table': 'campagne',
            },
        ),
        migrations.CreateModel(
            name='CampagneAppmobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('statut', models.CharField(choices=[('VALIDE', 'Valide'), ('SUPPRIME', 'Supprime'), ('BROUILLON', 'Brouillon'), ('CLOTURE', 'Cloture')], max_length=15, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('formulegarantie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.formulegarantie')),
                ('police', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.police')),
            ],
            options={
                'verbose_name': 'Campagne_appmobile',
                'verbose_name_plural': 'campagne_appmobile',
                'db_table': 'campagne_appmobile',
            },
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('prenoms', models.CharField(max_length=50, null=True)),
                ('nom_jeune_fille', models.CharField(max_length=100, null=True)),
                ('date_naissance', models.DateField(null=True)),
                ('lieu_naissance', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_securite_sociale', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_famille', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_ordre', models.CharField(blank=True, max_length=50, null=True)),
                ('matricule_employe', models.CharField(blank=True, max_length=50, null=True)),
                ('date_affiliation', models.DateField(blank=True, null=True)),
                ('date_sortie', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='prospects/')),
                ('statut_familiale', models.CharField(choices=[('M', 'Marie'), ('C', 'Celibataire'), ('D', 'Divorce'), ('', 'Choisir')], default='', max_length=15, null=True)),
                ('numero_piece', models.CharField(blank=True, max_length=50, null=True)),
                ('code_postal', models.CharField(blank=True, max_length=20, null=True)),
                ('ville', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone_fixe', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone_mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('rib', models.CharField(blank=True, max_length=50, null=True)),
                ('apci_ald', models.CharField(blank=True, max_length=50, null=True)),
                ('statut', models.CharField(choices=[('ACTIF', 'Actif'), ('INACTIF', 'Inactif')], default='ACTIF', max_length=15, null=True)),
                ('statut_enrolement', models.CharField(choices=[('EN ATTENTE', 'Attente'), ('EN COURS', 'Encours'), ('SOUMIS', 'Soumis'), ('VALIDE', 'Valide'), ('REJETE', 'Rejete'), ('INCORPORE', 'Incorpore')], default='EN ATTENTE', max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adherent_principal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='grh.prospect')),
                ('aliment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.aliment')),
                ('aliment_adherent_principal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='aliment_adherent_principal', to='production.aliment')),
                ('bureau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau')),
                ('civilite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.civilite')),
                ('formulegarantie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.formulegarantie')),
                ('pays_activite_professionnelle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pays_activite_professionnelle_prospect', to='configurations.pays')),
                ('pays_naissance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pays_naissance_prospect', to='configurations.pays')),
                ('pays_residence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pays_residence_prospect', to='configurations.pays')),
                ('police', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.police')),
                ('profession', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.profession')),
                ('qualite_beneficiaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.qualitebeneficiaire')),
            ],
            options={
                'verbose_name': 'Prospect',
                'verbose_name_plural': 'prospects',
                'db_table': 'prospects',
            },
        ),
        migrations.CreateModel(
            name='CampagneProspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien', models.CharField(max_length=255, null=True)),
                ('uiid', models.CharField(max_length=64, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('statut_enrolement', models.CharField(choices=[('EN ATTENTE', 'Attente'), ('EN COURS', 'Encours'), ('SOUMIS', 'Soumis'), ('VALIDE', 'Valide'), ('REJETE', 'Rejete'), ('INCORPORE', 'Incorpore')], default='EN ATTENTE', max_length=15, null=True)),
                ('campagne', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='grh.campagne')),
                ('prospect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='grh.prospect')),
            ],
        ),
        migrations.CreateModel(
            name='CampagneAppmobileProspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('statut_enrolement', models.CharField(choices=[('EN ATTENTE', 'Attente'), ('EN COURS', 'Encours'), ('SOUMIS', 'Soumis'), ('VALIDE', 'Valide'), ('REJETE', 'Rejete'), ('INCORPORE', 'Incorpore')], default='EN ATTENTE', max_length=15, null=True)),
                ('campagne_appmobile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='grh.campagneappmobile')),
                ('mouvement', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='production.mouvement')),
                ('prospect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='grh.prospect')),
            ],
        ),
    ]
