# Document file 1

## To add user in the database (MYSQL Database):

```
    CREATE USER "django"@"localhost" IDENTIFIED BY "password"; 
```

## To make changes to database (initial migration):

```
    py manage.py migrate
```

Note: Only those migrations are applied which are listed under INSTALLED_APPS in settings.py

refer : <a>https://docs.djangoproject.com/en/4.1/intro/tutorial02/</a>