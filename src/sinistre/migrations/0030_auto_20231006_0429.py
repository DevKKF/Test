# Generated by Django 3.2.15 on 2023-10-06 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0060_typeprefinancement'),
        ('sinistre', '0029_sinistre_taux_tm'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiersinistre',
            name='type_prefinancement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.typeprefinancement'),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='type_prefinancement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.typeprefinancement'),
        ),
    ]
