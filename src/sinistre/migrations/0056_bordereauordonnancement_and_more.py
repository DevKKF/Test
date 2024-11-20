# Generated by Django 4.0.3 on 2023-11-14 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configurations', '0074_typeremboursement_status'),
        ('sinistre', '0055_merge_20231114_1332'),
    ]

    operations = [

        migrations.AlterField(
            model_name='factureprestataire',
            name='statut',
            field=models.CharField(choices=[('ATTENTE', 'Attente'), ('VALIDE', 'Valide'), ('ORDONNANCE', 'Ordonnance'), ('PAYE', 'Paye'), ('ANNULE', 'Annule')], default='ATTENTE', max_length=30, null=True),
        ),
    ]