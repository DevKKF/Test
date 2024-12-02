# Generated by Django 3.2.19 on 2023-07-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0015_auto_20230719_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinistre',
            name='depassement',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='frais_reel',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='montant_plafond',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='part_assure',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='part_compagnie',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='plafond_chambre',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='plafond_hospit',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='ticket_moderateur',
            field=models.DecimalField(decimal_places=16, max_digits=31, null=True),
        ),
    ]
