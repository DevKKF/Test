# Generated by Django 3.2.15 on 2024-12-05 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0009_auto_20241205_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiquevehicule',
            name='formule',
        ),
        migrations.RemoveField(
            model_name='vehicule',
            name='formule',
        ),
    ]
