# Generated by Django 3.2.15 on 2024-10-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0127_cartedigitaldematerialisee'),
    ]

    operations = [
        migrations.AddField(
            model_name='reglement',
            name='banque_emettrice',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
