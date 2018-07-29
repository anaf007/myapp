#coding=utf-8
from main.helpers import templated,get_online_users
from flask_login import login_required
from flask import Response,current_app,copy_current_request_context
from flask_sse import sse
import psutil
from time import sleep
from . import bp
from main.extensions import executor


@templated()
def home():

    @copy_current_request_context
    def publish_cpu(flag=True):
        while flag:
            sse.publish({"cpu_use":psutil.cpu_percent()}, type='cpu_use',channel='admin')
            sleep(10)

    @copy_current_request_context
    def onlinr_users(flag=True):
        while flag:
            sse.publish({"count": str(len(get_online_users()) if len(get_online_users()) > 0 else 0)}, type='online',channel='admin')
            sleep(10)

    executor.submit(publish_cpu,True)
    executor.submit(onlinr_users,True)

    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')


    use_mem = mem.total-mem.available

    return dict(
        online_count=0,
        psutil=psutil,
        mem=mem,
        disk=disk,
        use_mem=use_mem//1024//1024
    )


# @login_required
@templated()
def index(name='admin'):
    return dict()


@login_required
@templated()
def web_site():
    return dict()



