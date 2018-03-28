from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django_datatables_view.base_datatable_view import BaseDatatableView

import httplib2
import subprocess
from collections import namedtuple
from ping.models import Hosts, Sites

class Server(object):
    def __init__(self):
        self.name = host.host_name

# Create your views here.
def index(request):
    hosts = Hosts.objects.order_by('host_name','category')
    prod = Hosts.objects.filter(category='prod')
    dev = Hosts.objects.filter(category='dev')
    misc = hosts.difference(prod, dev)
    for host in hosts:
        host.is_up = ping_server(host.host_name)
    for host in prod:
        host.is_up = ping_server(host.host_name)
        # print (host.host_name, host.category, '✅' if ping_server(host.host_name) else '❌')
    for host in dev:
        host.is_up = ping_server(host.host_name)
        # print (host.host_name, host.category, '✅' if ping_server(host.host_name) else '❌')
    for host in misc:
        host.is_up = ping_server(host.host_name)
        # print (host.host_name, host.category, '✅' if ping_server(host.host_name) else '❌')
    sites = Sites.objects.all()
    for each in sites:
        each.is_up = ping_website(each.url)
        # print(each.alias, each.category, '✅' if ping_website(each.url) else '❌')
    # return HttpResponse('Hello, world, this is the Ping app')
    template = loader.get_template('ping/ping.html')
    context = {
        'hosts': hosts,
        'prod': prod,
        'dev':  dev,
        'misc': misc,
        'sites': sites,
    }
    return HttpResponse(template.render(context,request))

def ping_server(host):
    'Pings given a host'
    return subprocess.getstatusoutput('ping -c 1 -t 10 %s' % host)[0] == 0

def ping_website(url):
    'Pings given website'
    try:
        return int(httplib2.Http().request(url, 'HEAD')[0]['status']) < 400
    except:
        pass
    try:
        return int(httplib2.Http().request(url.replace('https://','http://'), 'HEAD')[0]['status']) < 400
    except:
        pass
    return False
