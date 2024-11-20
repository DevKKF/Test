# Generated by Django 3.2.15 on 2023-12-05 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0081_auto_20231204_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compagnie',
            name='taux_com_courtage',
        ),
        migrations.RemoveField(
            model_name='compagnie',
            name='taux_com_gestion',
        ),
        migrations.AlterField(
            model_name='paramproduitcompagnie',
            name='compagnie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='taux_com', to='configurations.compagnie'),
        ),
    ]
