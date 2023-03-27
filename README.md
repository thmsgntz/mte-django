# mte-django
Refont of https://mathese-emoi.fr/ using Django framework

# Tools

- Bleeding edge django3.2 template focused on code quality and security:
    - Wemake-django: https://github.com/wemake-services/wemake-django-template
    - wemake-python: https://wemake-python-styleguide.readthedocs.io/en/latest/index.html
    - pre-commit: https://pre-commit.com
    - isort, autopep8, autoflake, docformatter, unify, flakeheaven

# API Access Objects

- QuerySets : https://docs.djangoproject.com/en/4.1/ref/models/querysets/#all
- Méthodes sur les relations https://docs.djangoproject.com/en/4.1/ref/models/relations/

# Admin

## Forget password
```python
from django.contrib.auth.models import User
User.objects.filter(is_superuser=True)

usr = User.objects.get(username='your username')
usr.set_password('raw password')
usr.save()
```

# Tutorial 2 -- Database (ok)
Lien -> https://docs.djangoproject.com/en/4.1/intro/tutorial02/

- Types objects : https://docs.djangoproject.com/en/4.1/ref/models/fields/

## Adding Annuaire in database (ok)

- Diagramme de classe fait dans [diagram](./diagrams).
- Migration faites (migrate, makemigrations, migrate)
- Ajout d'un objet avec l'onglet admin

## Migrations Database

1. `python manage.py migrate`
    > The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according
    > to the database settings in your mysite/settings.py file and the database migrations shipped with the app
    > (we’ll cover those later). You’ll see a message for each migration it applies.

2. `python manage.py makemigrations application_name`
   > By running `makemigrations`, you’re telling Django that you’ve made some changes to your models
   > (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

3. `python manage.py sqlmigrate application_name 0001`
   > let’s see what SQL that migration would run

4. `python manage.py migrate`
   > The migrate command takes all the migrations that haven’t been applied
   > (Django tracks which ones are applied using a special table in your database called django_migrations)
   > and runs them against your database - essentially, synchronizing the changes you made to your models
   > with the schema in the database.

# Tutorial 3 (ok polls only)
Lien -> https://docs.djangoproject.com/en/4.1/intro/tutorial03/

- URLdispatcher : https://docs.djangoproject.com/en/4.1/topics/http/urls/
> A clean, elegant URL scheme is an important detail in a high-quality web application.
> Django lets you design URLs however you want, with no framework limitations.

- Template Polls ([Write views that actually do something](https://docs.djangoproject.com/en/4.1/intro/tutorial03/#write-views-that-actually-do-something)) => Done

- Render Done (Index/Detail):
> The render() function takes the request object as its first argument, a template name as its second argument and a
> dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

- Removing hardcoded URLs in templates :
  - Dans polls/index.html:
  ```html
    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  ```
  - Dans polls/urls.py:
```python
from django.urls import path
from mte_website.polls import views
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
```
  - Du coup on peut utiliser le tag { % url } dans l'html :
  ```html
    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
  ```
  - Si on change l'url dans urls.py, pas d'action à faire dans le template html. Et c'est pris en compte.

- Namespacing URL names
  - Pour différencier les 'detail' de différentes app, on peut ajouter un namespace dans polls/urls.py:
  `app_name = 'polls'`
  - Puis dans html:
  `{% url 'detail' question.id %}`

# Tutorial 4 Forms (ongoing)
lien: https://docs.djangoproject.com/en/4.1/intro/tutorial04/

Next : [Use generic views: Less code is better](https://docs.djangoproject.com/en/4.1/intro/tutorial04/#use-generic-views-less-code-is-better)

# CSS SL

- [ ] first page: index qui redirige un accueil
- [ ] créer un onglet par application (permanence, blogs, annuaire..)
  - [ ] commencer par annuaire
- [ ] afficher les structures
- [ ] Mettre le CSS du site