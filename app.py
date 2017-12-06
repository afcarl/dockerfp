from flask import Flask, render_template
import docker
import re
from datetime import datetime
from pytz import timezone, utc


app = Flask(__name__)
app.config.from_object('settings')

TZ = timezone(app.config['DISPLAY_TZ'])

def map_cont(c):
    return {'name': c['Names'][0], 
            'created': datetime.fromtimestamp(c['Created'],utc).astimezone(TZ),
            'port': c['Ports'][0]['PublicPort'] if c['Ports'] else None}

@app.route('/')
def hello_world():
    client = docker.APIClient(base_url=app.config['DOCKER_SOCKET'])
    instances = map(map_cont,client.containers())
    instances = filter(lambda c: c['port'] and re.match(app.config['CONTAINER_RE'], c['name']), instances)
    return render_template("main.html", instances=instances )


