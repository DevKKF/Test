# Generated by Django 3.2.15 on 2024-06-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0188_auto_20240628_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupeCompagnie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('nom', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Groupe compagnie',
                'verbose_name_plural': 'Groupes de compagnies',
                'db_table': 'groupe_compagnie',
            },
        ),
        #migrations.RemoveField(
        #    model_name='acte',
        #    name='delais_carence',
        #),
        migrations.AddField(
            model_name='compagnie',
            name='groupe_compagnie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.groupecompagnie'),
        ),
    ]
