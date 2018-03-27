from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^(?P<network>[\w+]{2})/$', views.network_level),
    # re_path(r'^(?P<network>[\w+]{2})/(?P<station>\w+)/$', views.station_level),
]