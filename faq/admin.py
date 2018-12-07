from django.contrib import admin
from faq.models import *

# Register your models here.



class FAQAdmin(admin.ModelAdmin):
    list_display = ('bug_date','mold', 'ip', 'Duration_time', 'Sketch', 'process', 'prevention', 'remarks')
    search_fields = ('mold', 'ip', 'Duration_time', 'Sketch', 'process', 'prevention', 'remarks','bug_date')
    date_hierarchy = 'bug_date'
    ordering = ('-bug_date',)
    fields = ('mold', 'ip', 'Duration_time', 'Sketch', 'process', 'prevention', 'remarks','bug_date')

class YJGMAdmin(admin.ModelAdmin):
    list_display = ('bug_date','mold', 'parameter', 'Duration_time', 'Sketch','prevention','remarks')
    search_fields = ('mold', 'parameter', 'Duration_time', 'Sketch','prevention','remarks','bug_date')
    date_hierarchy = 'bug_date'
    ordering = ('-bug_date',)
    fields = ('mold', 'parameter', 'Duration_time', 'Sketch','prevention','remarks','bug_date')


admin.site.register(FAQ, FAQAdmin)
admin.site.register(YJGM, YJGMAdmin)
