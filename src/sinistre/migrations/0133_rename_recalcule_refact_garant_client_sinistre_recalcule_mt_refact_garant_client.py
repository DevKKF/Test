# Generated by Django 3.2.15 on 2024-09-23 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0132_auto_20240923_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sinistre',
            old_name='recalcule_refact_garant_client',
            new_name='recalcule_mt_refact_garant_client',
        ),
    ]