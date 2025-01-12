# Generated by Django 3.2.15 on 2023-10-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0069_typeprefinancement_statut'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeCreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('statut', models.CharField(choices=[('ACTIF', 'Actif'), ('INACTIF', 'Inactif')], default='ACTIF', max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mode de création',
                'verbose_name_plural': 'Modes de création',
                'db_table': 'mode_creation',
            },
        ),
    ]
