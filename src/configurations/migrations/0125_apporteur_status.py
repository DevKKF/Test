# Generated by Django 3.2.15 on 2023-12-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0124_auto_20231227_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='apporteur',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]