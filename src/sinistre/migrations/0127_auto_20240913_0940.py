# Generated by Django 3.2.15 on 2024-09-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0126_merge_20240912_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinistre',
            name='montant_refacture_client',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='montant_refacture_compagnie',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
    ]
