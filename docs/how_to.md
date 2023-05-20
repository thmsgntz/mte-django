
# Ajouter les onglets et les liens automatiquement

- Les onglets : Annuaire / A propos / Blog.. sont crées à partir des applications django.
- Les urls sont récupérés à partir du fichier urls.py de chaque app et recalculé avec un URL dispatcher.
- Un tag custom est créé, pour être utilisé dans l'html, qui renvoie un dictionnaire contenant le nom de l'onglet et son url

## Créer un Tag custom

Ajout d'un tag custom pour créer les urls pour chaque onglet 
- Placé dans `mte_website/templatetags/mte_website_extras.py`
- Il faut ensuite le register :
    - Dans le code `register = template.Library()` et décoration de la fonction `@register.simple_tag`
    - dans `settings.py`, ajouter dans la variable `TEMPLATE` le champ libraries: TEMPATE["libraries"]
    ```python
    TEMPLATES = [
    {
        # [...]
        'OPTIONS': {
            'libraries': {
                "mte_website_extras": "mte_website.templatetags.mte_website_extras"
            },
        },
    }]
    ```
- Puis dans l'html, appeler `{% load mte_website_extras %}` pour pouvoir faire : `{% custom_tag_function %}`

Liens :               
- https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/#howto-writing-custom-template-tags
- https://docs.djangoproject.com/en/4.2/topics/templates/#django.template.backends.django.DjangoTemplates 

## URL dispatcher 

Pour générer l'adresse automatiquement, deux choses à faire :
1. Dans l'application concernée (ex: annuaire) `annuaire.urls.py`, à la l'url voulu, définir un champ `name`
```python
    from django.urls import path
    import annuaire.views as views
    
    ANNUAIRE_INDEX_NAME = 'annuaire/index'  # le nom n'a pas d'importance !
    urlpatterns = [
        path('', views.index, name=ANNUAIRE_INDEX_NAME),
    ]
```

2. Utiliser l'url dispatcher pour générer l'url (exemple de custom tag de `mte_website.templatetags.mte_website_extras.py`):
```python
    from annuaire.urls import ANNUAIRE_INDEX_NAME
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    
    url = HttpResponseRedirect(reverse(ANNUAIRE_INDEX_NAME)).url
```

Liens :
- https://docs.djangoproject.com/en/4.2/topics/http/urls/#reverse-resolution-of-urls

## Dans Html

Le custom tag (`mte_website.templatetags.mte_website_extras.py`):

```python
from annuaire.urls import ANNUAIRE_INDEX_NAME
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import template
register = template.Library()

@register.simple_tag
def show_onglets():
onglets = [
{
    "name": "annuaire_func",

    # https://docs.djangoproject.com/en/4.2/topics/http/urls/#reverse-resolution-of-urls
    "val_href": HttpResponseRedirect(reverse(ANNUAIRE_INDEX_NAME)).url
},
{
    "name": "annuaire_func_2",
    "val_href": HttpResponseRedirect(reverse(ANNUAIRE_INDEX_NAME)).url
},
]
return onglets
```

L'html :

```html
{% load mte_website_extras %}

{% show_onglets as onglets %}
{% for onglet in onglets %}
<li>
    <a class="menu__link" href={{ onglet.val_href }}>
        {{ onglet.name }}
    </a>
</li>
{% endfor %}
```