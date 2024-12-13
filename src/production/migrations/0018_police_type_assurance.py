# Generated by Django 3.2.15 on 2024-12-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0005_remove_paramproduitcompagnie_taux_com_gestion'),
        ('production', '0017_remove_police_type_assurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='type_assurance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.typeassurance'),
        ),
    ]
