from flask import Flask
from tasks import *
import time

app = Flask(__name__)

def send_cons_tasks(N=1000):
    r = []
    for i in range(N):
        r.append(action.delay(i))

    while not all([x.ready() for x in r]):
        pass

@app.route("/")
def run():
    t1 = time.time()
    send_cons_tasks(10000)
    t2 = time.time()
    return str(t2 - t1)
