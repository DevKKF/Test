# Generated by Django 3.2.15 on 2024-02-06 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0149_auto_20240206_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='apporteur',
            name='type_personne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.typepersonne'),
        ),
    ]