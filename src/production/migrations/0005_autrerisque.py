# Generated by Django 3.2.15 on 2024-11-28 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0004_auto_20241128_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutreRisque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.client')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='ar_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('police', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.police')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='ar_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Autres Risques',
                'verbose_name_plural': 'Autres Risques',
                'db_table': 'autre_risque',
            },
        ),
    ]