#coding=utf-8
from main.helpers import templated
from flask_login import login_required



@templated()
def home(name='admin1'):
    return dict()


@login_required
@templated()
def index(name='admin'):
    return dict()