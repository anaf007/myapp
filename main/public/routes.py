#coding-utf-8
from main.helpers import LazyView
from . import blueprint,url


"""
url延迟加载
"""

#home
url('/', 'public.views.home')
#logout
url('/logout/','public.views.logout')
#register
url('/register/','public.views.register',methods=['GET', 'POST'])
#about
url('/about/','public.views.about')
#login
url('/login/','public.views.login',methods=['POST'])

