# django_with_celery_template

A starting point for and exercise in Celery and Django.

This project amalgamates what I've learnt from the Very Academy - Django Celery Mastery 
course into something more understandable.

The project has the potential to have other technologies in the same folder structure as
the Django project which has it's own directory (django).  

Within the django folder there is three component apps;
- core settings (no functionality),
- frontend (web including admin and dedicated elevated user functions),
- celery_worker (working within the same Django settings as the frontend).

This allows for separation of each Django code base.

The docker-compose.yml file builds a stack with three containers;
- the Django frontend app
- the Redis message broker
- the Celery worker built upon the Django settings.

This is a development implementation of these services in Docker.