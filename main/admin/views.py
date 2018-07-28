#coding=utf-8
from main.helpers import templated,get_online_users
from flask_login import login_required
from flask import Response
from flask_sse import sse

from . import bp

@templated()
def home():
    return dict()


# @login_required
@templated()
def index(name='admin'):
    return dict()


@login_required
@templated()
def web_site():
    return dict()



