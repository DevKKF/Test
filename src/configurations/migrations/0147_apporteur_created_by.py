# Generated by Django 3.2.15 on 2024-02-05 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0146_auto_20240205_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='apporteur',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
