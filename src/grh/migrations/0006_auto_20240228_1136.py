# Generated by Django 3.2.15 on 2024-02-28 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0081_policeclient'),
        ('grh', '0005_alter_campagneprospect_statut_enrolement'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagne',
            name='formulegarantie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.formulegarantie'),
        ),
        migrations.AddField(
            model_name='campagne',
            name='police',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.police'),
        ),
    ]
