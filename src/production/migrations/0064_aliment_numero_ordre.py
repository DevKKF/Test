# Generated by Django 3.2.15 on 2024-01-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0063_photoidentite'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliment',
            name='numero_ordre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]