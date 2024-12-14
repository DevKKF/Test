# Generated by Django 3.2.15 on 2024-11-27 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurations', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='client_grh',
            field=models.ManyToManyField(blank=True, related_name='client_grh', to='production.Client', verbose_name='Client (GRH)'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='prestataire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.prestataire'),
        ),
        migrations.AddField(
            model_name='user',
            name='type_utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.typeutilisateur'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='utilisateur_grh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.client', verbose_name='Client (GRH)'),
        ),
    ]
