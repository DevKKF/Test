# Generated by Django 3.2.15 on 2024-12-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0037_auto_20241226_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='autrerisque',
            name='date_liaison',
            field=models.DateTimeField(null=True),
        ),
    ]
