# django_with_celery_template

A starting point for other projects and a learning exercise in Celery and Django.

This project amalgamates what I've learnt from the Very Academy - Django Celery Mastery course into something more understandable.

The project has the potential to have other technologies in the same folder structure.  The Django project has it's own directory (django), while other non-Django code can be incorporated, e.g. the other_non_django_code builds an independent Celery worker, without access to Django.

Within the django folder there is three component apps;
- core settings (no functionality),
- frontend (web including admin and dedicated elevated user functions),
- celery_worker (working within the same Django settings as the frontend).

This allows for separation of each Django code base.

The docker-compose.yml file builds a stack with four containers;
- Django frontend app
- Redis message broker
- Celery worker built upon the Django settings.
- Celery worker that doesn't use Django.

This is a development implementation of these services in Docker.