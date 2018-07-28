# -*- coding: utf-8 -*-
"""The public module, including the homepage and user auth."""
from flask import Blueprint,session,request
from main.helpers import LazyView,mark_online,get_online_users
from flask_sse import sse

bp = Blueprint('public', __name__)

from . import routes,views  # noqa


@bp.before_request
def before_request():
    #在线人数统计
    mark_online(request.remote_addr)
    #回话超时登出
    session.permanent = True

    sse.publish({"count": str(len(get_online_users()) if len(get_online_users()) > 0 else 0)}, type='online')