# Generated by Django 3.2.15 on 2024-12-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0031_police_date_fin_effet'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='date_debut_effet',
            field=models.DateField(null=True),
        ),
    ]
