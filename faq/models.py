# -*- coding: UTF-8 -*-
from django.db import models

class FAQ(models.Model):
    mold = models.CharField(u'问题',max_length=80)
    ip = models.CharField(u'ip',max_length=50,blank=True)
    Duration_time = models.CharField(u'持续时间',max_length=20,blank=True)
    Sketch = models.CharField(u'简述',max_length=60)
    process = models.CharField(u'处理过程',max_length=100,blank=True)
    prevention = models.CharField(u'预防措施',max_length=500,blank=True)
    remarks = models.CharField(u'备注',max_length=500,blank=True)
    bug_date = models.DateField(u'故障日期', null=True )


    class Meta:
        db_table = 'record_FQA'
        verbose_name='故障记录'
        verbose_name_plural='线上故障记录'
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.mold,self.ip,self.Duration_time,self.Sketch,self.process,self.prevention,self.remarks,self.bug_date)


class YJGM(models.Model):
    mold = models.CharField(u'名称',max_length=200)
    parameter = models.CharField(u'规格参数',max_length=200,blank=True)
    Duration_time = models.CharField(u'价格',max_length=200,blank=True)
    Sketch = models.CharField(u'厂商维保',max_length=200,blank=True)
    prevention = models.CharField(u'序列号',max_length=200,blank=True)
    remarks = models.CharField(u'备注',max_length=500,blank=True)
    bug_date = models.DateField(u'购买日期', null=True )


    class Meta:
        db_table = 'record_YJGM'
        verbose_name='购买记录'
        verbose_name_plural='硬件购买记录'
    def __unicode__(self):
        return u'%s %s %s %s %s %s  %s' % (self.mold,self.parameter,self.Duration_time,self.Sketch,self.prevention,self.remarks,self.bug_date)
