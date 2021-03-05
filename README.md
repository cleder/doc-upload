# doc-upload

## Installation

Create a virtualenvironment with `python3 -m venv venv` and activate it with
`source venv/bin/activate`, upgrade pip with `pip install -U pip wheel` to the latest
version. Install the dependencies with `pip install -r requirements.txt`

Create models:
```
 python manage.py migrate
 python manage.py createsuperuser
 python manage.py runserver
```
