# Generated by Django 3.2.15 on 2023-09-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoActe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_assure', models.CharField(max_length=255, null=True)),
                ('medecin', models.CharField(max_length=255, null=True)),
                ('acte', models.IntegerField(null=True)),
                ('affection', models.CharField(max_length=100, null=True)),
                ('rc', models.CharField(max_length=255, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
