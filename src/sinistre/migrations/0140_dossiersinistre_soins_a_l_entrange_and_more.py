# Generated by Django 4.2.14 on 2024-11-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0139_historiquepaiementcomptablesinistre'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiersinistre',
            name='soins_a_l_entrange',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='soins_a_l_entrange',
            field=models.BooleanField(default=False),
        ),
    ]
