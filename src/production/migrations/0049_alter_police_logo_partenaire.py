# Generated by Django 3.2.15 on 2023-12-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0048_auto_20231225_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='logo_partenaire',
            field=models.ImageField(blank=True, null=True, upload_to='clients/polices/logos_partenaires/'),
        ),
    ]
