# Generated by Django 3.2.15 on 2024-02-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0080_alter_sinistre_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistre',
            name='statut_paiement',
            field=models.CharField(choices=[('EN ATTENTE', 'Attente'), ('ORDONNANCE', 'Ordonnance'), ('PAYE', 'Paye')], default='EN ATTENTE', max_length=15, null=True),
        ),
    ]
