from django.conf.urls import include, url, include
from django.contrib import admin
from rest_framework import routers
from case01 import views

router = routers.SimpleRouter()

router.register(r'student',views.StudentVS,base_name="stu")
urlpatterns = [
    # Examples:
    # url(r'^$', 'TlxyDRF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),



]
