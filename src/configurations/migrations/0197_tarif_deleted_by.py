# Generated by Django 3.2.15 on 2024-07-03 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0196_paramacte_entente_prealable'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarif',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='tarif_deleted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
