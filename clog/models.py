# -*- coding: UTF-8 -*- 
from django.db import models




class WYLOG(models.Model):
    time = models.DateTimeField(u'时间')
    deploy = models.CharField(u'项目',max_length=100)
    message = models.CharField(u'更新内容',max_length=1000)

    class Meta:
        db_table = 'WYLOG'
        verbose_name='微友更新说明'
        verbose_name_plural='微友更新说明'
    def __unicode__(self):
        return u'%s %s %s' % (self.time,self.deploy,self.message)
