#!/bin/ash

echo "This is the entrypoint.sh script."

# We can run anything here but this is just running the migrate, 
# which we could also do in the docker-compose.yml.
python manage.py migrate

# Execute and replace the command
exec "$@" 
