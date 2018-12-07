from django.contrib import admin
from Deployment_record.models import DEP
from Deployment_record.models import BACK
from Deployment_record.models import QD
from Deployment_record.models import DBBAK

class DEPAdmin(admin.ModelAdmin):
    list_display = ('time', 'deploy', 'war', 'message')
    search_fields = ('time', 'deploy', 'war', 'message')                                                                                                                                                                         
    date_hierarchy = 'time'
    ordering = ('-time',)
    fields = ('time', 'deploy', 'war', 'message')

class BACKAdmin(admin.ModelAdmin):
    list_display = ('time', 'deploy', 'message')
    search_fields = ('time', 'deploy', 'message')
    date_hierarchy = 'time'
    ordering = ('-time',)
    fields = ('time', 'deploy', 'message')

class QDAdmin(admin.ModelAdmin):
    list_display = ('time', 'deploy', 'message')
    search_fields = ('time', 'deploy', 'message')
    date_hierarchy = 'time'
    ordering = ('-time',)
    fields = ('time', 'deploy', 'message')

class DBBAKAdmin(admin.ModelAdmin):
    list_display = ('time', 'ip', 'way', 'xmm', 'md5l', 'md5r', 'message','iid')
    search_fields = ('time', 'ip', 'id')
#    date_hierarchy = 'time'
#    ordering = ('-time',)
    fields = ('time', 'ip', 'way', 'xmm', 'md5l', 'md5r', 'message', 'iid')

admin.site.register(DEP, DEPAdmin)
admin.site.register(BACK, BACKAdmin)
admin.site.register(QD, QDAdmin)
admin.site.register(DBBAK, DBBAKAdmin)
