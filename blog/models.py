# -*- coding: UTF-8 -*- 
from django.db import models


class IDC(models.Model):
    mold = models.CharField(u'服务',max_length=60)
    host = models.CharField(u'主机名',max_length=60,blank=True)
    ip = models.CharField(max_length=50)
    pw = models.CharField(u'密码',max_length=100,blank=True)
    dep = models.CharField(u'应用',max_length=60,blank=True)
    remarks = models.CharField(u'备注',max_length=400,blank=True)
    vm = models.CharField(u'宿主',max_length=300,blank=True)
    
    class Meta:
        db_table = 'record_machineroom'  
        verbose_name='记录'
        verbose_name_plural='IDC应用列表'
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s ' % (self.mold,self.host,self.ip,self.pw,self.dep,self.remarks,self.vm)
class GSIDC(models.Model):
    mold = models.CharField(u'型号',max_length=30)
    ip = models.CharField(max_length=50)
    port = models.CharField(max_length=20)
    uses = models.CharField(u'用途',max_length=60)
    account = models.CharField(u'账号',max_length=30)
    remarks = models.CharField(u'备注',max_length=200,blank=True)
    bug_date = models.DateField(u'购买日期',blank=True, null=True )

    class Meta:
        db_table = 'GongSi_machineroom'
        verbose_name='服务器记录'
        verbose_name_plural='公司机房登记'


    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.mold,self.ip,self.port,self.uses,self.account,self.remarks,self.bug_date)


class YJIDC(models.Model):
    jgmold = models.CharField(u'机柜号',max_length=20)
    mold = models.CharField(u'型号',max_length=20)
    no = models.CharField(u'机房编号',max_length=30)
    tp = models.CharField(u'类型',max_length=30,blank=True)
    hostname = models.CharField(u'主机名',max_length=30,blank=True)
    ip = models.CharField(max_length=50,blank=True)
    dep = models.CharField(max_length=20,blank=True)
    disk = models.CharField(u'硬盘',max_length=30,blank=True)
    memory = models.CharField(u'内存',max_length=30,blank=True)
    remarks = models.CharField(u'备注',max_length=200,blank=True)

    class Meta:
        db_table = 'YJIDC_machineroom'
        verbose_name='IDC记录'
        verbose_name_plural='IDC硬件统计'


    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s' % (self.jgmold,self.mold,self.no,self.tp,self.hostname,self.ip,self.dep,self.disk,self.memory,self.remarks)

class XSFW(models.Model):
    project = models.CharField(u'项目',max_length=20)
    dep = models.CharField(u'应用',max_length=60,blank=True)
    domain  = models.CharField(u'域名',max_length=80,blank=True)
    nginx  = models.CharField(u'分发器',max_length=80,blank=True)
    ip = models.CharField(max_length=80)
    port = models.CharField(max_length=20)
    memcache  = models.CharField(u'缓存地址',max_length=80,blank=True)
    remarks = models.CharField(u'备注',max_length=200,blank=True)
    class Meta:
        db_table = 'XSFW_machineroom'
        verbose_name='线上服务'
        verbose_name_plural='线上服务汇总'
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.project,self.dep,self.domain,self.nginx,self.ip,self.port,self.memcache,self.remarks)


