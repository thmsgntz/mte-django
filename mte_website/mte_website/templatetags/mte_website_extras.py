from typing import Callable, Dict, List

from accueil.urls import ACCUEIL_INDEX_NAME
from annuaire.urls import ANNUAIRE_INDEX_NAME
from blog.urls import BLOG_INDEX_NAME
from django import template
from django.http import HttpResponseRedirect
from django.urls import reverse

register = template.Library()


@register.simple_tag
def show_onglets() -> List[Dict[str, str]]:
    """Custom Templates used to generated les onglets automatiquement.

    Voir docs/how_to.md => ajout des onglets automatiquements


    https://docs.djangoproject.com/en/4.2/topics/http/urls/#reverse-resolution-of-urls
    """
    func: Callable[[str], str] = lambda url_str: str(HttpResponseRedirect(reverse(url_str)).url)

    return [
        {
            'name': 'accueil',
            # si l'application a un app_name, précisé "app_name:index_name"
            'val_href': func('accueil:{0}'.format(ACCUEIL_INDEX_NAME)),
        },
        {
            'name': 'annuaire',
            'val_href': func(ANNUAIRE_INDEX_NAME),
        },
        {
            'name': 'blog',
            'val_href': func(BLOG_INDEX_NAME),
        },
    ]
