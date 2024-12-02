# Generated by Django 4.1.7 on 2023-10-31 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sinistre', '0043_merge_20231030_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemboursementSinistre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=16, max_digits=50, null=True)),
                ('motif', models.CharField(blank=True, max_length=255, null=True)),
                ('statut', models.CharField(choices=[('ACCEPTE', 'Accepte'), ('REFUSE', 'Refuse')], default='REFUSE', max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('sinistre', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='remboursements', to='sinistre.sinistre')),
            ],
            options={
                'verbose_name': 'Remboursement',
                'verbose_name_plural': 'Remboursements',
                'db_table': 'remboursement_sinistre',
            },
        ),
    ]
