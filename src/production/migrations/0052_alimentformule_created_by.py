# Generated by Django 3.2.15 on 2023-12-30 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0051_client_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimentformule',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
