# -*- coding: utf-8 -*-
"""The public module, including the homepage and user auth."""
from flask import Blueprint,session
from main.helpers import LazyView

blueprint = Blueprint('public', __name__, static_folder='../static')

def url(url_rule, import_name, **options):
    view = LazyView('main.' + import_name)
    blueprint.add_url_rule(url_rule, view_func=view, **options)

from . import routes,views  # noqa

#回话超时登出
@blueprint.before_request
def make_session_permanent():
    session.permanent = True