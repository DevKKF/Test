# Generated by Django 3.2.15 on 2024-02-05 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0072_reglement_numero_piece'),
    ]

    operations = [
        migrations.AddField(
            model_name='quittance',
            name='observation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quittance',
            name='statut_validite',
            field=models.CharField(choices=[('VALIDE', 'Valide'), ('SUPPRIME', 'Supprime'), ('BROUILLON', 'Brouillon'), ('CLOTURE', 'Cloture')], default='VALIDE', max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='MouvementQuittance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.CharField(blank=True, max_length=255, null=True)),
                ('observation', models.CharField(blank=True, max_length=255, null=True)),
                ('date_effet', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('statut_validite', models.CharField(choices=[('VALIDE', 'Valide'), ('SUPPRIME', 'Supprime'), ('BROUILLON', 'Brouillon'), ('CLOTURE', 'Cloture')], default='VALIDE', max_length=15, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('mouvement', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='production.mouvement')),
                ('quittance', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='production.quittance')),
            ],
            options={
                'verbose_name': 'Mouvements sur la quittance',
                'verbose_name_plural': 'Mouvements sur les quittances',
                'db_table': 'mouvement_quittance',
            },
        ),
    ]