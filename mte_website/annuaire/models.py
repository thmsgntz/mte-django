from django.db import models


class Categorie(models.Model):
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre


class TagsStructure(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Structure(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    adresse_postale = models.CharField(max_length=200)
    phone = models.CharField('Numéro de Télphone', max_length=15)
    last_update = models.DateTimeField('Dernière Mise à jour', auto_now=True)
    mail = models.CharField('Adresse Email', max_length=30)
    tags = models.ManyToManyField(TagsStructure)
    categories = models.ManyToManyField(Categorie)

    def __str__(self):
        return self.nom
