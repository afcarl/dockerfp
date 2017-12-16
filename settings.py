# socket to connect to Docker Engine 
DOCKER_SOCKET = 'unix://var/run/docker.sock'
# will show only running containers that match this regular expression
CONTAINER_RE = '/pdf-checker'
# Show creation date and time of the container in this timezone
DISPLAY_TZ = 'Europe/Prague'
# Days after which cleanup.py script will delete containers
DEFAULT_CLEANUP_DAYS = 20
