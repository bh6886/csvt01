from django.contrib import admin
from blog.models import IDC
from blog.models import GSIDC
from blog.models import YJIDC
from blog.models import XSFW

class IDCAdmin(admin.ModelAdmin):
    list_display = ('mold', 'host', 'ip', 'pw','dep','remarks','vm')
    search_fields = ('mold', 'host', 'ip', 'pw','dep','remarks','vm')
    fields = ('mold', 'host', 'ip', 'pw', 'dep','remarks','vm')
class GSIDCAdmin(admin.ModelAdmin):
    list_display = ('mold', 'ip', 'port', 'uses', 'account', 'remarks', 'bug_date')
    search_fields = ('mold', 'ip', 'uses', 'account' , 'remarks')
    date_hierarchy = 'bug_date'
    ordering = ('-bug_date',)
    fields = ('mold', 'ip', 'port', 'uses', 'account', 'remarks','bug_date')
class YJIDCAdmin(admin.ModelAdmin):
    list_display = ('jgmold', 'mold', 'no', 'tp', 'hostname', 'ip', 'dep', 'disk', 'memory', 'remarks')
    search_fields = ('jgmold', 'mold', 'no', 'tp', 'hostname', 'ip', 'dep', 'disk', 'memory', 'remarks')
    fields = ('jgmold', 'mold', 'no', 'tp', 'hostname', 'ip', 'dep', 'disk', 'memory', 'remarks')

class XSFWAdmin(admin.ModelAdmin):
    list_display = ('project', 'dep', 'domain', 'nginx', 'ip', 'port', 'memcache', 'remarks')
    search_fields = ('project', 'dep', 'domain', 'nginx', 'ip', 'port', 'memcache', 'remarks')
    fields = ('project', 'dep', 'domain', 'nginx', 'ip', 'port', 'memcache', 'remarks')






admin.site.register(IDC, IDCAdmin)
admin.site.register(GSIDC, GSIDCAdmin)
admin.site.register(YJIDC, YJIDCAdmin)
admin.site.register(XSFW, XSFWAdmin)
