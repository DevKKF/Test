# Generated by Django 3.2.15 on 2023-11-28 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0064_alter_sinistre_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sinistre',
            options={'permissions': [('can_do_saisie_prestataire', 'Peut saisir des PEC en ligne'), ('can_do_saisie_gestionnaire', 'Peut saisir des PEC physiques'), ('can_view_prestations', 'Peut afficher les PEC'), ('can_do_generation_bordereau_facturation', 'Peut générer un bordereau de facturation'), ('can_view_bordereaux_facturations', 'Peut voir bordereaux de facturations'), ('can_view_facturesprestataires_en_attente', 'Peut voir les factures prestataire en attente'), ('can_view_facturesprestataires_validees', 'Peut voir les factures prestataire validées'), ('can_do_traitement_factures_prestataire', 'Peut traiter les factures prestataires'), ('can_view_remboursements_validees', 'Peut voir les remboursements validées'), ('can_do_ordonnancement', 'Peut faire un ordonnancement'), ('can_view_bordereaux_ordonnancement', "Peut voir les bordereaux d'ordonnancements")], 'verbose_name': 'Sinistre', 'verbose_name_plural': 'Sinistres'},
        ),
    ]
