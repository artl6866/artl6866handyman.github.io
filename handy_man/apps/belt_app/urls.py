from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.main),
    url(r'^/add$', views.add),
    url(r'^/processadd$', views.processadd),
    url(r'^/show/(?P<id>\d+)$', views.show),
    url(r'^/delete/(?P<id>\d+)$', views.delete),
    url(r'^/edit/(?P<id>\d+)$', views.edit),
    url(r'^/updatejob/(?P<id>\d+)$', views.updatejob),
    url(r'^/join/(?P<id>\d+)$', views.join),
    # url(r'^/remove/(?P<id>\d+)$', views.remove),

    
    
    
]