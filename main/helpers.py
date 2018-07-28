#coding=utf-8

from werkzeug import import_string, cached_property
from functools import wraps
from flask import request,render_template,session,current_app
from datetime import timedelta


#延迟加载视图
class LazyView(object):

    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)


def url(bp,url_rule, import_name, **options):
    view = LazyView('main.' + bp.name+'.views.'+ import_name)
    bp.add_url_rule(url_rule, view_func=view, **options)



#模板装饰器
def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator





