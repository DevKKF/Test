# Generated by Django 3.2.15 on 2024-05-02 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0167_bureau_commentaire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bureau',
            old_name='commentaire',
            new_name='mention_legale',
        ),
    ]
