# Generated by Django 3.2.15 on 2024-05-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0103_auto_20240516_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinistre',
            name='date_paiement',
            field=models.DateField(blank=True, null=True),
        ),
    ]
