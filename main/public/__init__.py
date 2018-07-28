# -*- coding: utf-8 -*-
"""The public module, including the homepage and user auth."""
from flask import Blueprint,session
from main.helpers import LazyView

bp = Blueprint('public', __name__)

from . import routes,views  # noqa

#回话超时登出
@bp.before_request
def make_session_permanent():
    session.permanent = True