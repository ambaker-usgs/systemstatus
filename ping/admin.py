from django.contrib import admin

from .models import Hosts, Sites

# Register your models here.
admin.site.register(Hosts)
admin.site.register(Sites)