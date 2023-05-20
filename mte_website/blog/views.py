# Create your views here.
from typing import Any

from django.http import HttpResponse


def index(request: Any) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the Blogs index.")
