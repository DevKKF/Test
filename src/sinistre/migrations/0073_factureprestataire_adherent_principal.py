# Generated by Django 3.2.15 on 2024-01-19 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0061_delete_photoidentite'),
        ('sinistre', '0072_alter_sinistre_aliment'),
    ]

    operations = [
        migrations.AddField(
            model_name='factureprestataire',
            name='adherent_principal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.aliment'),
        ),
    ]