# Generated by Django 3.2.15 on 2024-08-22 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0205_merge_20240821_1634'),
        ('production', '0117_auto_20240822_0955'),
        ('sinistre', '0115_merge_20240822_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanderemboursementmobile',
            name='adherent_principal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.aliment'),
        ),
        migrations.AlterField(
            model_name='demanderemboursementmobile',
            name='bureau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau'),
        ),
    ]
