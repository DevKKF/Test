# Generated by Django 3.2.15 on 2024-12-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0028_auto_20241222_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marchandise',
            old_name='adresse',
            new_name='adresse_commissaire',
        ),
        migrations.RenameField(
            model_name='marchandise',
            old_name='code',
            new_name='code_commissaire',
        ),
        migrations.RenameField(
            model_name='marchandise',
            old_name='courriel',
            new_name='courriel_commissaire',
        ),
        migrations.RenameField(
            model_name='marchandise',
            old_name='nom',
            new_name='nom_commissaire',
        ),
        migrations.RenameField(
            model_name='marchandise',
            old_name='telephone',
            new_name='telephone_commissaire',
        ),
        migrations.AddField(
            model_name='autrerisque',
            name='date_du_jour',
            field=models.DateTimeField(null=True),
        ),
    ]
