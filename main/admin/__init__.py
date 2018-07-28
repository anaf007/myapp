#coding=utf-8

from flask import Blueprint,session
from main.helpers import LazyView

bp = Blueprint('admin', __name__,url_prefix='/admin')

from . import routes,views,models

#回话超时登出
@bp.before_request
def make_session_permanent():
    session.permanent = True
