# Generated by Django 3.2.15 on 2024-10-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0224_compagnie_code_courtier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compagnie',
            name='code_courtier',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
