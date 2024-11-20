# Generated by Django 3.2.19 on 2023-06-25 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_bareme_periodicite'),
        ('sinistre', '0004_sinistre_served_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistre',
            name='bareme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.bareme'),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='formulegarantie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.formulegarantie'),
        ),
    ]
