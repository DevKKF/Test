# Generated by Django 3.2.15 on 2023-11-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0032_alter_police_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='logo_partenaire',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]