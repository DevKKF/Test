# Generated by Django 3.2.15 on 2024-02-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0142_bureau_option_export_beneficiaires'),
    ]

    operations = [
        migrations.AddField(
            model_name='apporteur',
            name='id_per',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='apporteur',
            name='code',
            field=models.CharField(blank=True, default=None, max_length=25, null=True, unique=True),
        ),
    ]