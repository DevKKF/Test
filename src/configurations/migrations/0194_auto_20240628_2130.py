# Generated by Django 3.2.15 on 2024-06-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0193_auto_20240628_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='apporteurveos',
            name='NUM_SOC',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
