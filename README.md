# doc-upload

## Installation

Create a virtualenvironment with `python3 -m venv venv` and activate it with
`source venv/bin/activate`, upgrade pip with `pip install -U pip wheel` to the latest
version. Install the dependencies with `pip install -r requirements.txt`

Create a PostgreSQL database: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

Create a file `local_settings.py` in the directory `doccenter` to connect to the database.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Initialize the database and start the server:
```
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver
```

Navigate to [localhost:8000](http://localhost:8000).

The django admin interface is available on [localhost:8000/admin/](http://localhost:8000/admin/).
