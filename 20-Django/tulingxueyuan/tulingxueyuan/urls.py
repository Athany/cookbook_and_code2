# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv

from teacher import teacher_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 视图函数名称只有名称，无括号和参数
    url(r'^normalmap/',tv.do_normalmap),

    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),
    # 比如约定，凡是有teacher模块处理的视图的url都以teacher开头
    url(r'^teacher/', include(teacher_url)),

    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),

    url(r'^yourname/$',tv.extremParam,{"name":"liudana"}),

    url(r'^mayiknowyourname/$', tv.revParse, name="askname"),
]
