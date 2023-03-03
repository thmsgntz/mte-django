# mte-django
Refont of https://mathese-emoi.fr/ using Django framework

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
   