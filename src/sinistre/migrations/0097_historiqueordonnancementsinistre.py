# Generated by Django 3.2.15 on 2024-04-16 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sinistre', '0096_bordereauordonnancement_bo_deleted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriqueOrdonnancementSinistre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=16, max_digits=50, null=True)),
                ('observation', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borderau_ordonnancement', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sinistre.bordereauordonnancement')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('sinistre', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sinistre.sinistre')),
            ],
            options={
                'verbose_name': 'Historique ordonnancement sinistre',
                'verbose_name_plural': 'Historique ordonnancement sinistre',
                'db_table': 'historique_ordonnancement_sinistre',
            },
        ),
    ]
