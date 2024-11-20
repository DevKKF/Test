# Generated by Django 3.2.15 on 2023-12-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0101_auto_20231214_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quittanceveos',
            name='DATE_DEBUT',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quittanceveos',
            name='DATE_EMIS',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quittanceveos',
            name='DATE_FIN',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quittanceveos',
            name='DATE_SITUATION_APPORTEUR',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quittanceveos',
            name='DATE_SITUATION_CLIENT',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quittanceveos',
            name='DATE_SITUATION_COMPAGNIE',
            field=models.DateField(blank=True, null=True),
        ),
    ]
