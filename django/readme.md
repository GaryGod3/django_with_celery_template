This project amalgamates what I've learnt from the Very Academy - Django Celery Mastery 
course into something more understandable.

The project has the potential to have other technologies in the same folder structure as
the Django project has it's own directory.  Within the Django folder there is three component apps;
- core settings,
- frontend (web including admin and dedicated elevated user functions),
- celery_worker.

This allows for separation of each Django code base.

The docker-compose.yml file builds a stack with three containers;
- the Django frontend app
- the Redis message broker
- the Celery worker built upon the Django settings.

It is a development implementation of these services in Docker.