# Generated by Django 3.2.15 on 2024-11-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banque',
            name='nom_complet',
            field=models.TextField(blank=True, null=True),
        ),
    ]
