from celery import Celery, Task
import time
import ctypes
from celeryconfig import *

app = Celery('tasks')
app.config_from_object('celeryconfig')

class CallbackTask(Task):
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print('finished')

@app.task(base=CallbackTask)
def action(i):
    'short task'
    return 42

# @app.task(base=CallbackTask)
# def action(i):
#     'long task'
#     time.sleep(10)
#     return 42

# @app.task(base=CallbackTask)
# def action(i):
#     'high cpu task'
#     a = len(str(math.factorial(100000)))
#     return 42

# @app.task(base=CallbackTask)
# def action(i):
#     'high I/O task'
#     f = open("%s.txt" % str(i), 'w')
#     f.write('0'*10**9)
#     f.close()
#     return 42
