# Generated by Django 4.1.7 on 2023-11-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0072_auto_20231030_1532'),
        ('sinistre', '0047_merge_20231103_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiersinistre',
            name='prestataire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='dossiers_sinistres', to='configurations.prestataire'),
        ),
        migrations.AlterField(
            model_name='factureprestataire',
            name='statut',
            field=models.CharField(choices=[('ATTENTE', 'Attente'), ('ATTENTE ORDONNANCEMENT', 'Attente Ordonnancement'), ('PAYE', 'Paye'), ('ANNULE', 'Annule')], default='ATTENTE', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='remboursementsinistre',
            name='statut',
            field=models.CharField(choices=[('ACCEPTE', 'Accepte'), ('REFUSE', 'Refuse'), ('NET A PAYER', 'Net A Payer'), ('TAXT', 'Taxt')], default='REFUSE', max_length=15, null=True),
        ),
    ]
