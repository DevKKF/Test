# Generated by Django 3.2.19 on 2023-07-25 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0030_auto_20230725_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionlog',
            name='data_after',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actionlog',
            name='data_before',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlog',
            name='table',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]