# Steps to create a django project:

## Initialize a python env and start it (windows only):

```
    python -m venv venv
    venv\Scripts\activate
```

## Install Django and create project:

```
    pip install django
```

### or install from requirements.txt file:

```
    pip install -r requirements.txt
```

## Create a project:

```
    django-admin startproject project
```

## Run the project server (localhost:8080):

```
    cd project
    py manage.py runserver 8080
```

## Create app in Django (in project dir):

```
    py manage.py startapp <app_name>
```

### Example:

```
    py manage.py startapp login
```