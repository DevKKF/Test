# Generated by Django 3.2.15 on 2023-10-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0029_auto_20231012_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulegarantie',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]