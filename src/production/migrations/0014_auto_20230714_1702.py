# Generated by Django 3.2.19 on 2023-07-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0013_alter_aliment_date_naissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliment',
            name='nom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aliment',
            name='prenoms',
            field=models.CharField(max_length=50, null=True),
        ),
    ]