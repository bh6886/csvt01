# -*- coding: UTF-8 -*- 
from django.db import models



class DEP(models.Model):
    time = models.DateTimeField(u'部署时间')
    deploy = models.CharField(u'所属工程',max_length=100)
    war = models.CharField(u'包名',max_length=600)
    message = models.CharField(u'信息',max_length=600)
    
    class Meta:
        db_table = 'Deployment_record'  
        verbose_name='部署记录'
        verbose_name_plural='TTS部署记录'
    def __unicode__(self):
        return u'%s %s %s %s' % (self.time,self.deploy,self.war,self.message)


class BACK(models.Model):
    time = models.DateTimeField(u'时间')
    deploy = models.CharField(u'所属工程',max_length=100)
    message = models.CharField(u'信息',max_length=600)

    class Meta:
        db_table = 'Rollback_record'
        verbose_name='回滚记录'
        verbose_name_plural='TTS回滚记录'
    def __unicode__(self):
        return u'%s %s %s' % (self.time,self.deploy,self.message)


class QD(models.Model):
    time = models.DateTimeField(u'时间')
    deploy = models.CharField(u'所属工程',max_length=100)
    message = models.CharField(u'信息',max_length=1000)

    class Meta:
        db_table = 'QD_record'
        verbose_name='前端部署'
        verbose_name_plural='前端部署记录'
    def __unicode__(self):
        return u'%s %s %s' % (self.time,self.deploy,self.message)

class DBBAK(models.Model):
    time =  models.CharField(u'时间',max_length=10)
    ip = models.CharField(u'ip',max_length=20)
    way = models.CharField(u'备份方式',max_length=13)
    xmm = models.CharField(u'项目名',max_length=10)
    md5l = models.CharField(u'本地md5',max_length=50,blank=True,null=True)
    md5r = models.CharField(u'异地md5',max_length=50,blank=True,null=True)
    message = models.CharField(u'md5验证',max_length=6,blank=True,null=True)
    iid = models.CharField(max_length=10)

    class Meta:
        db_table = 'DB_backup'
        verbose_name='数据库备份'
        verbose_name_plural='数据库备份记录'
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s' % (self.time,self.ip,self.way,self.xmm,self.md5l,self.md5r,self.message,self.iid)
