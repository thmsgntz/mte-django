# Generated by Django 4.1.3 on 2023-02-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TagsStructure',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nom', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('adresse_postale', models.CharField(max_length=200)),
                (
                    'phone',
                    models.CharField(
                        max_length=15, verbose_name='Numéro de Télphone',
                    ),
                ),
                (
                    'last_update',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Dernière Mise à jour',
                    ),
                ),
                ('mail', models.CharField(max_length=30, verbose_name='Adresse Email')),
                ('categories', models.ManyToManyField(to='annuaire.categorie')),
                ('tags', models.ManyToManyField(to='annuaire.tagsstructure')),
            ],
        ),
    ]
