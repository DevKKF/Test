# Generated by Django 3.2.15 on 2023-12-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0121_acte_lettre_cle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acte',
            name='lettre_cle',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
