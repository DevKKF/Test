# Generated by Django 3.2.15 on 2024-12-13 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0007_alter_branche_table'),
        ('production', '0023_policegarantie_formule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('lien_fichier', models.CharField(blank=True, max_length=50, null=True)),
                ('service', models.CharField(choices=[('production', 'Production'), ('sinistre', 'Sinistre'), ('comptabilite', 'Comptabilité')], max_length=50)),
                ('status', models.CharField(choices=[('Actif', 'Actif'), ('Inactive', 'Inactive')], default='Inactif', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.produit')),
            ],
            options={
                'db_table': 'production_courrier',
            },
        ),
    ]