#!/bin/bash                                                                                                                                                                                                       

# NAME - Name of the application
# DEP - Deployment name
# DEPDIR - Deployment directory
# USER - the user to run as
# GROUP -  the group to run as
# NUM_WORKERS - how many worker processes should Gunicorn spawn
# VENV_DIR - virtual env dir
# IP - IP address to bind
# PORT - PORT to bind
# TIMEOUT - timeout
# MAX_REQUESTS - The maximum number of requests a worker will process before restarting

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $VENV_DIR
source ./bin/activate

# Jump to djangodir
cd $DEPDIR

# Start your Django Unicorn                                                                                                                                                                                       # Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)                                                                                                                  
exec  gunicorn $DEP.wsgi:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --max-requests $MAX_REQUESTS \
  --limit-request-line $LIMIT_REQUEST_LINE \
  --user=$USER --group=$GROUP \
  --bind=${IP}:${PORT} \
  --timeout $TIMEOUT \
#  --log-level=debug \   