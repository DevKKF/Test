# Generated by Django 3.2.19 on 2023-06-20 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_typeprestataire_code'),
        ('sinistre', '0002_alter_sinistre_statut_prestation'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiersinistre',
            name='centre_prescripteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='centre_prescripteur', to='configurations.prestataire'),
        ),
    ]
