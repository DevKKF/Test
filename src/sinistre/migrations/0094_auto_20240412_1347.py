# Generated by Django 3.2.15 on 2024-04-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0093_auto_20240411_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiersinistre',
            name='date_reception_facture',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dossiersinistre',
            name='reference_facture',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]