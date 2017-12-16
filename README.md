Simple web application, that will show all running docker containers with certain name pattern
and provide a http link to then ( to first published port).

How to use
----------

* Edit settings.py 
* Deploy app in WSGI server (application must have access to Docker Engine socket)

Deployment with nginx and uwsgi
-------------------------------

Not very secure so should be used only on internal networks for testing (uwsgi socket has world rw acces)

nginx site configuration:
```
location / {
		include uwsgi_params;
		uwsgi_pass unix:/tmp/uwsgi.sock;
		uwsgi_read_timeout 300;

	}
```

uwsgi ini file:
```
[uwsgi]
plugin = python
socket = /tmp/uwsgi.sock
chmod-socket = 666
chdir = /path/to/dockerfp
module = app
callable = app
uid = your_user_with_docker_access
gid = your_user_with_docker_access
```

