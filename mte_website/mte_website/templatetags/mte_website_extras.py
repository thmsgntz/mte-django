from typing import Dict, List

from annuaire.urls import ANNUAIRE_INDEX_NAME
from django import template
from django.http import HttpResponseRedirect
from django.urls import reverse

register = template.Library()


@register.simple_tag
def show_onglets() -> List[Dict[str, str]]:
    return [
        {
            'name': 'annuaire_func',
            # https://docs.djangoproject.com/en/4.2/topics/http/urls/#reverse-resolution-of-urls
            'val_href': HttpResponseRedirect(reverse(ANNUAIRE_INDEX_NAME)).url,
        },
        {
            'name': 'annuaire_func_2',
            'val_href': HttpResponseRedirect(reverse(ANNUAIRE_INDEX_NAME)).url,
        },
    ]
