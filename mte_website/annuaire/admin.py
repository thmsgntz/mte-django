from django.contrib import admin

from .models import Categorie, Structure, TagsStructure

# Register your models here.

admin.site.register(Categorie)
admin.site.register(TagsStructure)
admin.site.register(Structure)
