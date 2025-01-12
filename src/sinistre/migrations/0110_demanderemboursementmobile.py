# Generated by Django 3.2.15 on 2024-07-26 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0110_merge_20240726_1026'),
        ('configurations', '0198_auto_20240703_1638'),
        ('sinistre', '0109_paiementcomptable_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeRemboursementMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sinistre', models.DateField()),
                ('montant_a_rembourser', models.DecimalField(decimal_places=2, max_digits=20)),
                ('numero_remboursement', models.CharField(blank=True, max_length=100, null=True)),
                ('prescription_medical', models.FileField(upload_to='prescriptions/')),
                ('facture_normalisee', models.FileField(upload_to='factures/')),
                ('acquittee_laboratoire', models.FileField(upload_to='acquittees/')),
                ('autre_document', models.FileField(blank=True, null=True, upload_to='autres/')),
                ('statut', models.CharField(choices=[('EN ATTENTE', 'Attente'), ('DEMANDE', 'Demande'), ('ACCEPTE', 'Accepte'), ('ACCEPTE PARTIELLEMENT', 'Accepte Partiellement'), ('REFUSE', 'Refuse'), ('ANNULE', 'Annule')], default='EN ATTENTE', max_length=25, null=True)),
                ('acte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.acte')),
                ('adherent_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adherent_principal_remboursements', to='production.aliment')),
                ('beneficiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiaire_remboursements', to='production.aliment')),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.bureau')),
                ('mode_remboursement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.modereglement')),
                ('prestataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.prestataire')),
            ],
            options={
                'verbose_name': 'Demande de remboursement mobile',
                'verbose_name_plural': 'Demandes de remboursement mobiles',
                'db_table': 'demande_remboursement_mobile',
            },
        ),
    ]
