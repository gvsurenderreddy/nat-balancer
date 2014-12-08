from django.contrib import admin
from models import *

class HostModelAdmin(admin.ModelAdmin):
    list_display = ('name','address')
admin.site.register(Host, HostModelAdmin)

class TunnelModelAdmin(admin.ModelAdmin):
    list_display = ('name','address','interface', 'status')
admin.site.register(Tunnel, TunnelModelAdmin)
