# Generated by Django 3.2.15 on 2024-12-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0024_courrier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiquepolice',
            name='garantie',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('', 'Choisir')], max_length=10, null=True),
        ),
    ]
