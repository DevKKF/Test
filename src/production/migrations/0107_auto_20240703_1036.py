# Generated by Django 3.2.15 on 2024-07-03 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0106_merge_20240703_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quittance',
            options={'permissions': [('can_do_annulation_quittance', 'Peut annuler des quittances')], 'verbose_name': 'Quittance', 'verbose_name_plural': 'Quittances'},
        ),
        migrations.AddField(
            model_name='quittance',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='quittance_deleted_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reglement',
            name='reg_deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='reg_deleted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]