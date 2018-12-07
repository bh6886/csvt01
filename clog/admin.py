from django.contrib import admin
from clog.models import WYLOG

class WYLOGAdmin(admin.ModelAdmin):
    list_display = ('time', 'deploy', 'message')
    search_fields = ('time', 'deploy', 'message')
    date_hierarchy = 'time'
    ordering = ('-time',)
    fields = ('time', 'deploy', 'message')

admin.site.register(WYLOG, WYLOGAdmin)
