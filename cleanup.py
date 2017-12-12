import sys
import re
import time
import docker
import settings


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else settings.DEFAULT_CLEANUP_DAYS
    client = docker.APIClient(base_url=settings.DOCKER_SOCKET)
    containers = client.containers(all=True)
    for container in containers:
        if re.match(settings.CONTAINER_RE, container['Names'][0]) and \
        time.time() - container['Created'] > days * 24 * 3600:
            client.remove_container(container['Id'],force=True)
            client.remove_image(container['Image'])

    #client.prune_images()



if __name__ == '__main__':
    main()