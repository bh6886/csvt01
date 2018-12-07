#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import loader, Context, Template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import os,sys,MySQLdb
import glob,upyun
import re
import datetime,time
import platform
import urllib,urllib2,paramiko,shutil,pexpect
import logging
from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required


from random import Random
from multiprocessing import Process
import httplib
import simplejson as json

import json
import zookeeper
from clog.models import WYLOG
now_time = datetime.datetime.now()
t =  now_time.strftime('%Y-%m-%d')

logger = logging.getLogger(__name__)

#def login(request):
#    if request.method == 'POST':
#            username = request.POST['username']
#            password = request.POST['password']
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                if user.is_active:
#                            user_login(request, user)
#                            return HttpResponseRedirect('/index.html')
#                else:
#                    return HttpResponse('用户没有启用!')
#            else:
#                return HttpResponse('用户名或者密码错误！')
#    else:
#        return render_to_response('login.html')
#


def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            if username == 'test':
                return HttpResponse('该账户禁止登录前台!')
            else:
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                                user_login(request, user)
                                return HttpResponseRedirect('/index.html')
                    else:
                        return HttpResponse('用户没有启用!')
                else:
                    return HttpResponse('用户名或者密码错误！')
    else:
        return render_to_response('login.html')










def loginout(request):
    user_logout(request)
    return HttpResponseRedirect('/')


def time():
  now_time = datetime.datetime.now()
  t =  now_time.strftime('%Y-%m-%d')
  return t

def DB1(sql):
   conn = MySQLdb.connect(user='root',passwd='taotaosou',host='192.168.3.31',charset='utf8')
   cur = conn.cursor()
   conn.select_db('csvt')
   AA = cur.execute(sql)
   AA = cur.fetchmany(AA)
   cur.close()
   conn.commit()
   conn.close()
   return AA

#@login_required
#def index(req):
#  now_time = datetime.datetime.now()
#  t =  now_time.strftime('%Y-%m-%d %H:%M:%S')
#  time = [t]
#  logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#  return render_to_response('index.html',{'title':'taotaosou','time':time})

@login_required
def index(req):
  now_time = datetime.datetime.now()
  t =  now_time.strftime('%Y-%m-%d %H:%M:%S')
  RQ = now_time.strftime('%Y-%m-%d')
  yes_time1 = now_time + datetime.timedelta(days=-1)
  RQ1 = yes_time1.strftime('%Y-%m-%d')

  yes_time2 = now_time + datetime.timedelta(days=-2)
  RQ2 = yes_time2.strftime('%Y-%m-%d')

  yes_time3 = now_time + datetime.timedelta(days=-3)
  RQ3 = yes_time3.strftime('%Y-%m-%d')

  yes_time4 = now_time + datetime.timedelta(days=-4)
  RQ4 = yes_time4.strftime('%Y-%m-%d')

  yes_time5 = now_time + datetime.timedelta(days=-5)
  RQ5 = yes_time5.strftime('%Y-%m-%d')

  yes_time6 = now_time + datetime.timedelta(days=-6)
  RQ6 = yes_time6.strftime('%Y-%m-%d')

  yes_time7 = now_time + datetime.timedelta(days=-7)
  RQ7 = yes_time7.strftime('%Y-%m-%d')
  time = [t]
  sql = '''select time,ip,xmm,message from DB_backup ORDER BY time DESC LIMIT 10;'''
  sql1 = '''select count(*) from DB_backup where message = 'true';'''
  sql2 = '''select count(*) from DB_backup where message  is null;'''
  sql3 = '''select count(*) from DB_backup where message = 'false';'''
  sql4 = '''select ip from disk;'''
  sql5 = '''select stime,num from stime ORDER BY stime DESC LIMIT 7;'''
  sql6 = '''select ym,pv,uv,sdate from domain where sdate = '%s';'''%RQ
  SS1 = DB1(sql)
  SS2 = DB1(sql1)[0][0]
  SS3 = DB1(sql2)[0][0]
  SS4 = DB1(sql3)[0][0]
  SS5 = DB1(sql4)
  SS6 = DB1(sql5)
  SS7 = DB1(sql6)
  os.chdir('/opt/csvt01/logs')
#  aa = os.popen("grep -E 'register|cp' all.log |grep -v 'bohan' | awk '{ print  $6 }' > /tmp/phtmp.txt").read().strip()
  aa = os.popen("grep -E 'register|cp' all.log |grep -v 'bohan'|grep -v 'test'| awk '{ print  $6 }' > /tmp/phtmp.txt").read().strip()
  res = []
  fileName = file('/tmp/phtmp.txt')
  while True:
    line = fileName.readline()
    if len(line) ==0:break
    a = line.split('-')[1]
    res.append(a)
  fileName.close()
  a = {}
  for i in res:
    if res.count(i)>1:
      a[i] = res.count(i)
  def fun(s):
      d = sorted(s.iteritems(),key=lambda t:t[1],reverse=True)
      return d
  d = fun(a)
  logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
  return render_to_response('index.html',{'title':'taotaosou','time':time,'SS1':SS1,'SS2':SS2,'SS3':SS3,'SS4':SS4,'SS5':SS5,'SS6':SS6,'d':d,'RQ1':RQ1,'RQ2':RQ2,'RQ3':RQ3,'RQ4':RQ4,'RQ5':RQ5,'RQ6':RQ6,'RQ7':RQ7,'SS7':SS7,'RQ':RQ})



def TEST(A,B):

 url_str = A
 url_status = dict()

 def is_url(url):
        try:
                html = urllib2.urlopen(url).read()
                return html.find(url_str)
        except:
                return "Request Url Error"

 for url in open(B):
        url =url.strip("\n")
        if url != "":
                for i in range(1, 2):
                        num = is_url(url)
                        if not isinstance(num, str):
                                #print num
                                if num >= 0:
                                        url_status[url] = "正常"
                                        break
                                else:
                                        url_status[url] = "错误，请检查"
                        else:
                                url_status[url] = num
 TT = []
 for key in url_status.keys():
        TT.append("%s 接口为 %s" %(key, url_status[key]))
 return  TT  

def www(req):
 TT = TEST('taotaosou','/opt/csvt01/url/www.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def app(req):
 TT = TEST('taotaosou','/opt/csvt01/url/app.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def client(req):
 TT = TEST('chaoji99','/opt/csvt01/url/client.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def item(req):
 TT = TEST('去购买','/opt/csvt01/url/item.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def search(req):
 TT = TEST('女包','/opt/csvt01/url/search.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def service(req):
 TT = TEST('www.taotaosou.com','/opt/csvt01/url/service.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

 
def tejia(req):
 TT = TEST('tejia.taotaosou.com','/opt/csvt01/url/tejia.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def tuan(req):
 TT = TEST('tuan.taotaosou.com','/opt/csvt01/url/tuan.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def dapei(req):
 TT = TEST('dapei.taotaosou.com','/opt/csvt01/url/dapei.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})
 
def sitemap(req):
 TT = TEST('泳衣','/opt/csvt01/url/sitemap.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def br(req):
 TT = TEST('JSP','/opt/csvt01/url/br.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def recom(req):
 TT = TEST('item.taobao.com','/opt/csvt01/url/recom.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def showmold(req):
 TT = TEST('res','/opt/csvt01/url/showmold.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def showapp(req):
 TT = TEST('Hello Boy','/opt/csvt01/url/showapp.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})
 

def showeng(req):
 TT = TEST('Hello Boy','/opt/csvt01/url/showeng.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA}) 


def control(req):
 TT = TEST('status','/opt/csvt01/url/control.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def cmsproxy(req):
 TT = TEST('this is a test page for cms proxy service','/opt/csvt01/url/cmsproxy.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def seckill(req):
 TT = TEST('seckill server','/opt/csvt01/url/seckill.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def pay_web(req):
 TT = TEST('body','/opt/csvt01/url/pay_web.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

def trade_web(req):
 TT = TEST('body','/opt/csvt01/url/trade_web.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def chaoji99(req):
 TT = TEST('chaoji99','/opt/csvt01/url/chaoji99.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def app99(req):
 TT = TEST(']','/opt/csvt01/url/app99.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def sso(req):
 TT = TEST('sendsms.do','/opt/csvt01/url/sso.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})


def sp(req):
 TT = TEST('依赖如下','/opt/csvt01/url/sp.txt')
 AA = len(TT)
 return render_to_response('showmold.html',{'TT':TT,'AA':AA})

########################################################################################### 

def do_post(img,img1,img2,img3):
  params = urllib.urlencode({'username': 'taotaosou-cdn', \
                             'password' : '<^^XS$3VZy', \
                             'task': '{"urls":[""] ,\
                                       "dirs":["%s","%s","%s","%s"],\
                             "callback" : {"url":"","email" : [ "bohan@taotaosou.com" ], "acptNotice": true}}' % (img,img1,img2,img3)})
  f = urllib.urlopen("http://r.chinacache.com/content/refresh" , params)
  return  f.code
  #print f.read()


def do_post1(img):
  params = urllib.urlencode({'username': 'taotaosou-cdn', \
                             'password' : '<^^XS$3VZy', \
                             'task': '{"urls":[""] ,\
                                       "dirs":["%s"],\
                             "callback" : {"url":"","email" : [ "bohan@taotaosou.com" ], "acptNotice": true}}' % img})
  f = urllib.urlopen("http://r.chinacache.com/content/refresh" , params)
  return  f.code
  #print f.read()
##########################################################################################
@login_required
def autowww(req):
 dir = u'/nfsdata/bohan/sypt-super/www/'
 auto = u'/home/app/auto_file/tts/tts-www-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n') 
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/autowww.html',{'title':'autowww','aa':aa})


class UserForm(forms.Form):
    name = forms.CharField()
@login_required
def register(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/www/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                #print remotepath 
                #print localpath
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    return render_to_response('register.html',{'form':form})

@login_required
def depwww121(req):
 ip = '10.0.0.121'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/www.py')
 child.expect('@')
 deyy = child.before  
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'depwww','ss':ss})

@login_required
def depwww80(req):
 ip = '192.168.3.80'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/www.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'depwww','ss':ss})

@login_required
def depwww81(req):
 ip = '192.168.3.81'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/www.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'depwww','ss':ss})

class UserForm(forms.Form):       
    name = forms.CharField()   
@login_required
def registerapp(req):                
    if req.method == 'POST':   
        form = UserForm(req.POST) 
        if form.is_valid():       
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/app/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                #print remotepath 
                #print localpath
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    return render_to_response('register.html',{'form':form})
    
	
#autoconfig
@login_required
def autoapp(req):
 dir = u'/nfsdata/bohan/sypt-super/app/'
 auto = u'/home/app/auto_file/tts/tts-app-service-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 os.popen("chmod  777 %s" % WAR).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})

###dep###
@login_required
def depapp121(req):
 ip = '10.0.0.121'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/app.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def depapp186(req):
 ip = '192.168.3.186'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/app.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def depapp22(req):
 ip = '10.0.0.22'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/app.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

##################################client#########################################
class UserForm(forms.Form):
    name = forms.CharField()
@login_required
def registerclient(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/client/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

#autoconfig

@login_required
def autoclient(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/client/'         #chage
 auto = u'/home/app/auto_file/tts/tts-client-service-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa}) 

@login_required
def zzbsclient(req):			#chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-client.html',{'title':'zzbs'})  #chage

###dep###

@login_required
def depclient186(req):   #chage
 ip = '192.168.3.186'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/client.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})


@login_required
def depclient22(req):  
 ip = '10.0.0.22'    

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/client.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def depclient183(req):   #chage
 ip = '10.0.0.183'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/client.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def depclient51(req):   #chage
 ip = '10.0.0.51'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/client.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})


@login_required
def registeritem(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/item/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})
#autoconfig

@login_required
def autoitem(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/item/'         #chage
 auto = u'/home/app/auto_file/tts/tts-item-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})
@login_required
def zzbsitem(req):			#chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-item.html',{'title':'zzbs'})  #chage

@login_required
def depitem59(req):  #chage
 ip = '10.0.0.59'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/item.py')  #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def depitem17(req):   #chage
 ip = '192.168.3.17'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/item.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def depitem37(req):  #chage
 ip = '192.168.3.37'  #chage   

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/item.py')  #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})


@login_required
def registersearch(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/search/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#autoconfig

@login_required
def autosearch(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/search/'         #chage
 auto = u'/home/app/auto_file/tts/tts-search-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})
@login_required
def zzbssearch(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-search.html',{'title':'zzbs'})  #chage


@login_required
def depsearch17(req):   #chage
 ip = '192.168.3.17'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/search.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def depsearch37(req):  
 ip = '192.168.3.37'    

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/search.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def registerservice(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/service/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

#autoconfig

@login_required
def autoservice(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/service/'         #chage
 auto = u'/home/app/auto_file/tts/tts-app-service-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})

@login_required
def zzbsservice(req):                    #chage
 return render_to_response('auto/zzbs-service.html',{'title':'zzbs'})  #chage

###dep###

@login_required
def depservice22(req):   #chage
 ip = '10.0.0.22'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/service.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def depservice52(req):  
 ip = '10.0.0.52'    

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/service.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def depservice59(req):
 ip = '10.0.0.59'

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/service.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})


#########################################tejia_dep################################################
@login_required
def registertejia(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/tejia/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#autoconfig


@login_required
def zzbstejia(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-tejia.html',{'title':'zzbs'})  #chage
@login_required
def autotejia(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/tejia/'         #chage
 auto = u'/home/app/auto_file/tts/tts-tejia-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})




###dep###

@login_required
def deptejia19(req):   #chage
 ip = '192.168.3.19'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/tejia.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def deptejia18(req):  
 ip = '192.168.3.18'    

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/tejia.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
#########################################tuan_dep################################################
@login_required
def registertuan(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/tuan/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#autoconfig


@login_required
def zzbstuan(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-tuan.html',{'title':'zzbs'})  #chage
@login_required
def autotuan(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/tuan/'         #chage
 auto = u'/home/app/auto_file/tts/tts-tuan-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})

###dep###

@login_required
def deptuan18(req):   #chage
 ip = '192.168.3.18'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/tuan.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def deptuan19(req):  
 ip = '192.168.3.19'    

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/tuan.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})


#########################################sitemap_dep################################################
@login_required
def registersitemap(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/sitemap/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#autoconfig
@login_required
def autositemap(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/sitemap/'         #chage
 auto = u'/home/app/auto_file/tts/tts-sitemap-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-sitemap.html',{'title':'autositemap','aa':aa})    #chage
@login_required
def zzbssitemap(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})

###dep###

@login_required
def depsitemap80(req):   #chage
 ip = '192.168.3.80'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/sitemap.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})

@login_required
def depsitemap83(req):  
 ip = '192.168.3.83'    

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/sitemap.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})


#########################################dapei_dep################################################
@login_required
def registerdapei(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/dapei/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#autoconfig
@login_required
def autodapei(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/dapei/'         #chage
 auto = u'/home/app/auto_file/tts/tts-dapei-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto.html',{'title':'www','aa':aa})

@login_required
def zzbsdapei(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-dapei.html',{'title':'zzbs'})  #chage

###dep###

@login_required
def depdapei106(req):   #chage
 ip = '192.168.3.106'  #chage

 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/dapei.py')   #chage
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def depdapei37(req):  
 ip = '192.168.3.37'    
 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/dapei.py') 
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
@login_required
def depdapei80(req):
 ip = '192.168.3.80'
 child = pexpect.spawn('ssh -t -p 58022 %s sudo su - app' % ip)
 child.expect('@')
 child.sendline('/home/app/shell/dapei.py')
 child.expect('@')
 deyy = child.before
 ss = deyy.split('\n')
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/dep-bijia.html',{'title':'www','ss':ss})
################check tomcat log tail -n 200#############################################
def ssh(ip,port,user,shell1,shell2):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user)
        channel = ssh.invoke_shell()
        channel.settimeout(60)
        channel.send('%s\n' % shell1)
        buff = ''
        while not buff.endswith('$ '):
            resp = channel.recv(9999)
            buff +=resp
        buff = ''
        channel.send('%s\n' % shell2)
        while not buff.endswith('$ '):
            resp = channel.recv(9999)
            buff +=resp
        result = buff
        return result
        ssh.close()

def ssh1(ip,port,user,shell1,shell2):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user)
        channel = ssh.invoke_shell()
        channel.settimeout(60)
        channel.send('%s\n' % shell1)
        buff = ''
        while not buff.endswith('# '):
            resp = channel.recv(9999)
            buff +=resp
        buff = ''
        channel.send('%s\n' % shell2)
        while not buff.endswith('# '):
            resp = channel.recv(9999)
            buff +=resp
        result = buff
        return result
        ssh.close()

def logindex(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/log_index.html',{'title':'log_index'})  #chage

def logindex1(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/log_index1.html',{'title':'log_index1'})  #chage
@login_required
def registerbijiadep(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/bijiadep/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/bijiadep/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('auto/register-bijiadep.html',{'form':form})  #chage
@login_required
def zzbsbijiadep(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-bijiadep.html',{'title':'zzbs'})  #chage
@login_required
def autoconfig(dir,auto):          #chage
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 os.popen("chmod -R 777 %s" % WAR).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 #os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return aa

@login_required
def bijiadep_auto(req):
       aa = autoconfig('/nfsdata/bohan/sypt-super/bijiadep/','/home/app/auto_file/bijia/auto.browser.properties')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/auto.html',{'title':'autoconfig','aa':aa}) 
@login_required
def bijiadep_183(req):
       sun = ssh('10.0.0.183',58022,'bohan','sudo su - app','/home/app/shell/bohan.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})       
@login_required
def bijiadep_94(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','/home/app/shell/bohan.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})  
@login_required
def bijiadep_83(req):
       sun = ssh('192.168.3.83',58022,'bohan','sudo su - app','/home/app/shell/bohan.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss}) 
@login_required
def bijiadep_48(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','/home/app/shell/bohan.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss}) 
@login_required
def bijiadep_51(req):
       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','/home/app/shell/bohan.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})
@login_required
def bijiadep_183_wc(req):
       sun = ssh('10.0.0.183',58022,'bohan','sudo su - app','for a in 8{1..4}80;do netstat -na |grep $a |grep  CLOSE_WAIT  |wc -l;done')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})       
@login_required
def bijiadep_94_wc(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','for a in 8{1..3}80;do netstat -na |grep $a |grep  CLOSE_WAIT  |wc -l;done')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})  
@login_required
def bijiadep_83_wc(req):
       sun = ssh('192.168.3.83',58022,'bohan','sudo su - app','for a in 9{1..3}80;do netstat -na |grep $a |grep  CLOSE_WAIT  |wc -l;done')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss}) 
@login_required
def bijiadep_48_wc(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','for a in 8{1..3}80;do netstat -na |grep $a |grep  CLOSE_WAIT  |wc -l;done')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss}) 
@login_required
def bijiadep_51_wc(req):
       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','for a in 8{1..3}80;do netstat -na |grep $a |grep  CLOSE_WAIT  |wc -l;done')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})

###################################################recom###########################################
@login_required
def registerrecomdep(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/recomdep/*.war')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/recomdep/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
@login_required
def zzbsrecomdep(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-recomdep.html',{'title':'zzbs'})  #chage
#@login_required
#def recomdep_auto(req):
#       aa = autoconfig('/nfsdata/bohan/sypt-super/recomdep/',' /home/app/auto_file/bijia/auto.browser-recom.properties')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/auto.html',{'title':'autoconfig','aa':aa})
@login_required
def recomdep_23(req):
       sun = ssh('192.168.3.101',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/engine_bs.py recom /home/app/tomcat-7.0.27-browser-recom-6180/ browser-recom-6180 /nfsdata/bohan/sypt-super/recomdep/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

@login_required
def recomdep_51(req):
       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/engine_bs.py recom /home/app/tomcat-7.0.27-browser-recom-6180/ browser-recom-6180 /nfsdata/bohan/sypt-super/recomdep/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

#@login_required
#def recomdep_23(req):
#       sun = ssh('192.168.3.101',58022,'bohan','sudo su - app','/home/app/shell/bohan1.py')
#       ss = sun.split('\n')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/dep-bijia.html',{'title':'log-recomcs','ss':ss})       
#@login_required
#def recomdep_51(req):
#       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','/home/app/shell/bohan1.py')
#       ss = sun.split('\n')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/dep-bijia.html',{'title':'log-recomcs','ss':ss})  
#@login_required
#def recomdep_23_wc(req):
#       sun = ssh('10.0.0.101',58022,'bohan','sudo su - app','/home/app/shell/jkport.sh')
#       ss = sun.split('\n')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/dep-bijia.html',{'title':'log-recomcs','ss':ss})       
#@login_required
#def recomdep_51_wc(req):
#       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','/home/app/shell/jkport.sh')
#       ss = sun.split('\n')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/dep-bijia.html',{'title':'log-recomcs','ss':ss})  
@login_required
def autoconfig1(dir,auto):          #chage
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 os.popen("chmod -R 777 %s" % WAR).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return aa
@login_required
def registercontroldep(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/controldep/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
@login_required
def zzbscontroldep(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-controldep.html',{'title':'zzbs'})  #chage
@login_required
def controldep_auto(req):
       aa = autoconfig1('/nfsdata/bohan/sypt-super/controldep/',' /home/app/auto_file/tts/tts-control-autoconfig.properties')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/auto.html',{'title':'autoconfig','aa':aa})
@login_required
def controldep_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/home/app/shell/control.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-controlcs','ss':ss})
@login_required
def controldep_19(req):
       sun = ssh('192.168.3.19',58022,'bohan','sudo su - app','/home/app/shell/control.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-controlcs','ss':ss})


#############################################################qianduan###################################################
@login_required
def registerqdtmtdep(req):   
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/tmt/'   
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
@login_required
def zzbstmtdep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-tmt.html',{'title':'zzbs'})  #chage
@login_required
def qdtmtdep_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/qdtmt.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdtmtcs','ss':ss})       
def qdtmtdep_118(req):
       sun = ssh('10.0.0.118',58022,'bohan','sudo su - app','tkdown')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdtmtcs','ss':ss})  
@login_required
def registerqdtaobaodep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/taobao/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def zzbstaobaodep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-taobao.html',{'title':'zzbs'})  #chage	
@login_required
def qdtaobaodep_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/qdtaobao.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdtaobaocs','ss':ss})       
def qdtaobaodep_118(req):
       sun = ssh('10.0.0.118',58022,'bohan','sudo su - app','tkdown')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdtaobaocs','ss':ss})  
	   
@login_required
def registerexttaobaodep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/ext/taobao/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

@login_required
def registerexttmtdep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/ext/tmt/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
@login_required
def ext_taobao_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/ext/ext_taobao.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextcs','ss':ss})
@login_required
def cdn_exttaobao_post(req):
       ss = do_post1("http://ext.taotaosou.com/browser-static/taobao/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})

@login_required
def ext_tmt_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/ext/ext_tmt.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextcs','ss':ss})
@login_required
def cdn_exttmt_post(req):
       ss = do_post1("http://ext.taotaosou.com/browser-static/tmt/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})
@login_required
def registerextstaobaodep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/exts/taobao/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

@login_required
def registerextstmtdep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/exts/tmt/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
@login_required
def exts_taobao_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/exts/exts_taobao.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextscs','ss':ss})

@login_required
def exts_tmt_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/exts/exts_tmt.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextscs','ss':ss})

@login_required
def registerqdqdstatdep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qdstat/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def zzbsqdstatdep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-qdstat.html',{'title':'zzbs'})  #chage      
@login_required
def qdqdstatdep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/home/app/shell/qdtts.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdqdstatcs','ss':ss})
def qdqdstatdep_7(req):
       sun = ssh('10.0.0.7',58022,'bohan','sudo su - app','/home/app/rs-data.sh')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdqdstatcs','ss':ss})
@login_required
def cdn_qdstat_post(req):
       ss = do_post("http://img.taotaosou.cn/tts1-static/","http://img01.taotaosou.cn/tts1-static/","http://img02.taotaosou.cn/tts1-static/","http://img03.taotaosou.cn/tts1-static/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})

################################################################################################
@login_required
def registerqdchaoji99dep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qdchaoji99/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def zzbchaoji99dep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-qdchaoji99.html',{'title':'zzbs'})  #chage      
@login_required
def qdchaoji99dep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/home/app/shell/qdchaoji99.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdchaoji99cs','ss':ss})
def qdchaoji99dep_7(req):
       sun = ssh('10.0.0.7',58022,'bohan','sudo su - app','/home/app/rs-data.sh')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdchaoji99cs','ss':ss})
@login_required
def cdn_qdchaoji99_post(req):
       ss = do_post("http://img.taotaosou.cn/tts-99/","http://img01.taotaosou.cn/tts-99/","http://img02.taotaosou.cn/tts-99/","http://img03.taotaosou.cn/tts-99/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})

##############################################cmsproxy#######################
@login_required
def registercmsproxydep (req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/cmsproxy/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

@login_required
def zzbscmsproxydep(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-cmsproxydep.html',{'title':'zzbs'})  #chage


@login_required
def cmsprxoydep_22(req):
       sun = ssh('10.0.0.22',58022,'bohan','sudo su - app','/home/app/shell/cmsproxy.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})
@login_required
def cmsprxoydep_23(req):
       sun = ssh('10.0.0.23',58022,'bohan','sudo su - app','/home/app/shell/cmsproxy.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})
@login_required
def cmsprxoydep_83(req):
       sun = ssh('192.168.3.83',58022,'bohan','sudo su - app','/home/app/shell/cmsproxy.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})
	   
@login_required
def cmsproxydepdel(req):
       sun = ssh('10.0.0.51',58022,'bohan','sudo su - bohan','rm -rf /nfsdata/bohan/sypt-super/cmsproxy/*.war')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-cmsproxycs','ss':ss})

############################################cms############################################
@login_required
def registercmsdep (req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/cms/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

@login_required
def zzbscmsdep(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-cmsdep.html',{'title':'zzbs'})  #chage


@login_required
def cmsdep_121(req):
       sun = ssh('10.0.0.121',58022,'bohan','sudo su - app','/home/app/shell/cms.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-bijiacs','ss':ss})
######################################################################################
@login_required
def registerseckill(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/seckill/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def autoseckill(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/seckill/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autoseckill','aa':aa})    #chage
@login_required
def zzbsseckill(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-seckill.html',{'title':'zzbs'})  #chage

@login_required
def seckilldep_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','/home/app/shell/seckill.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'seckill','ss':ss})
@login_required
def seckilldep_81(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','/home/app/shell/seckill.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'seckill','ss':ss})
###########################################################################################
@login_required
def registerpay_web(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/pay_web/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def autopay_web(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/pay_web/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autopay_web','aa':aa})    #chage
@login_required
def zzbspay_web(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-pay_web.html',{'title':'zzbs'})  #chage

@login_required
def pay_webdep_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','/home/app/shell/pay_web.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'pay_web','ss':ss})
@login_required
def pay_webdep_81(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','/home/app/shell/pay_web.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'pay_web','ss':ss})


##############################################################################################
@login_required
def registertrade_web(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/trade_web/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def autotrade_web(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/trade_web/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autotrade_web','aa':aa})    #chage
@login_required
def zzbstrade_web(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-trade_web.html',{'title':'zzbs'})  #chage

@login_required
def trade_webdep_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','/home/app/shell/trade_web.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'trade_web','ss':ss})
@login_required
def trade_webdep_81(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','/home/app/shell/trade_web.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'trade_web','ss':ss})
#############################################################################################
@login_required
def registertradeback(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/tradeback/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def autotradeback(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/tradeback/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autotradeback','aa':aa})    #chage
@login_required
def zzbstradeback(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-tradeback.html',{'title':'zzbs'})  #chage

@login_required
def tradebackdep_81(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','/home/app/shell/tradeback.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tradeback','ss':ss})

############################################################################################
@login_required
def registerp4p_mgr(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4p_mgr/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def autop4p_mgr(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/p4p_mgr/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autop4p_mgr','aa':aa})    #chage
@login_required
def zzbsp4p_mgr(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-p4p_mgr.html',{'title':'zzbs'})  #chage
@login_required
def p4p_mgrdep_11(req):
       sun = ssh('192.168.3.11',58022,'bohan','sudo su - app','/home/app/shell/p4p_mgr.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})


#####################################################################################
@login_required
def registerp4p_add(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4p_add/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def autop4p_add(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/p4p_add/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autop4p_add','aa':aa})    #chage
@login_required
def zzbsp4p_add(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-p4p_add.html',{'title':'zzbs'})  #chage
@login_required
def p4p_adddep_11(req):
       sun = ssh('192.168.3.11',58022,'bohan','sudo su - app','/home/app/shell/p4p_add.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_add','ss':ss})

#######################################################################################
@login_required
def registerp4p_dlsproxy(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/p4p_dlsproxy/*.war')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4p_dlsproxy/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


@login_required
def p4p_dlsproxydep_11(req):
       sun = ssh('192.168.3.11',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py p4p /home/app/tomcat-7.0.27-p4p-proxy-8780/ p4p-proxy-8780 /nfsdata/bohan/sypt-super/p4p_dlsproxy/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})
@login_required
def p4p_dlsproxyhg_11(req):
       sun = ssh('192.168.3.11',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py p4p /home/app/tomcat-7.0.27-p4p-proxy-8780/ p4p-proxy-8780')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})
@login_required
def p4p_dlsproxylog_11(req):
       sun = ssh('192.168.3.11',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-p4p-proxy-8780/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

########################################################################################
@login_required
def registercmsproxy_monitor(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/cmsproxy_monitor/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



def autocmsproxy_monitor(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/cmsproxy_monitor/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autocmsproxy_monitor','aa':aa})    #chage

def zzbscmsproxy_monitor(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-cmsproxy_monitor.html',{'title':'zzbs'})  #chage

def cmsproxy_monitordep_24(req):
       sun = ssh('192.168.3.24',58022,'bohan','sudo su - app','/home/app/shell/cmsproxy_monitor.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'cmsproxy_monitor','ss':ss})
##############################################chaoji99################
@login_required
def registerchaoji99(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/chaoji99/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


#autoconfig
def zzbschaoji99(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-chaoji99.html',{'title':'zzbs'})  #chage

def autochaoji99(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/chaoji99/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "chaoji99  is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'chaoji99','aa':aa})    #chage
 


def chaoji99_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/home/app/shell/chaoji99.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})
def chaoji99_19(req):
       sun = ssh('192.168.3.19',58022,'bohan','sudo su - app','/home/app/shell/chaoji99.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})
def chaoji99_121(req):
       sun = ssh('10.0.0.121',58022,'bohan','sudo su - app','/home/app/shell/chaoji99.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})
#######################################i.taoji99.com#########################################
@login_required
def registerchaoji99_i(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/chaoji99_i/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


#autoconfig
def zzbschaoji99_i(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-chaoji99_i.html',{'title':'zzbs'})  #chage

def autochaoji99_i(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/chaoji99_i/'         #chage
 auto = u'/home/app/auto_file/tts/tts-i-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-dapei.html',{'title':'autochaoji99_i','aa':aa})    #chage


def chaoji99_i_121(req):
       sun = ssh('10.0.0.121',58022,'bohan','sudo su - app','/home/app/shell/chaoji99_i.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})	   
	   
def chaoji99_i_22(req):
       sun = ssh('10.0.0.22',58022,'bohan','sudo su - app','/home/app/shell/chaoji99_i.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})

##########################################################################################################s
@login_required
def registerapp99(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/app99/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


#autoconfig
def zzbsapp99(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-app99.html',{'title':'zzbs'})  #chage

def autoapp99(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/app99/'         #chage
 auto = u'/home/app/auto_file/tts/tts-tuan-autoconfig.properties'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-dapei.html',{'title':'autoapp99','aa':aa})    #chage

def app99_38(req):
       sun = ssh('10.0.0.38',58022,'bohan','sudo su - app','/home/app/shell/app99.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})
def app99_46(req):
       sun = ssh('10.0.0.46',58022,'bohan','sudo su - app','/home/app/shell/app99.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'p4p_mgr','ss':ss})

 
#########################################################################################
@login_required
def registerqdtts_kmeyedep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qdtts-kmeye/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



def zzbtts_kmeyedep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-qdtts_kmeye.html',{'title':'zzbs'})  #chage      
def qdtts_kmeyedep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/home/app/shell/tts-kmeye.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log_qdtts_kmeyecs','ss':ss})
def qdtts_kmeyedep_7(req):
       sun = ssh('10.0.0.7',58022,'bohan','sudo su - app','/home/app/rs-data.sh')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log_qdtts_kmeyecs','ss':ss})

def cdn_kmeyedep_post(req):
       ss = do_post("http://img.taotaosou.cn/tts-kmeye/","http://img01.taotaosou.cn/tts-kmeye/","http://img02.taotaosou.cn/tts-kmeye/","http://img03.taotaosou.cn/tts-kmeye/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})



##############################################################################################
@login_required
def registerqly(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qly/*.war')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



def zzbsqly(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-qly.html',{'title':'zzbs'})  #chage

def qlydep_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly /home/app/tomcat-7.0.27-tts_qly-8480/ tts_qly-8480  /nfsdata/bohan/sypt-super/qly/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlydep_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly /home/app/tomcat-7.0.27-tts_qly-8480/ tts_qly-8480  /nfsdata/bohan/sypt-super/qly/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})


def qlyhg_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-tts_qly-8480/ tts_qly-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlyhg_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-tts_qly-8480/ tts_qly-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlylog_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-tts_qly-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlylog_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-tts_qly-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})


@login_required
def qly_restart_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','~/shell/restart.sh tts_qly 8480  restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def qly_restart_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','~/shell/restart.sh tts_qly 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



def qlydep_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly /home/app/tomcat-7.0.27-tts_qly-8480/ tts_qly-8480  /nfsdata/bohan/sypt-super/qly/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlyhg_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-tts_qly-8480/ tts_qly-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlylog_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-tts_qly-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

def qlyjavakill_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/java_kill.py tts_qly-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly','ss':ss})

##########################################################################################
@login_required
def registerqdv7dep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qdv7/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



def zzbv7dep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-qdv7.html',{'title':'zzbs'})  #chage      
def qdv7dep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/home/app/shell/v7.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log_qdv7cs','ss':ss})
def qdv7dep_7(req):
       sun = ssh('10.0.0.7',58022,'bohan','sudo su - app','/home/app/rs-data.sh')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log_qdv7cs','ss':ss})

def cdn_qdv7_post(req):
       ss = do_post("http://img.taotaosou.cn/tts-mobile/v7/","http://img01.taotaosou.cn/tts-mobile/v7/","http://img02.taotaosou.cn/tts-mobile/v7/","http://img03.taotaosou.cn/tts-mobile/v7/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})

####################################################################################
@login_required
def registersso(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/sso/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/sso/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



#def autosso(req):          #chage
# dir = u'/nfsdata/bohan/sypt-super/sso/'         #chage
# auto = u'xxx'
# list = os.listdir(dir)
# for line in list:
#     filepath = os.path.join(dir,line)
#     if os.path.isfile(filepath):
#         WAR = filepath
## AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
# aa = "tts_client is not autoconfig, complete copy!!!"
# BAOM = os.path.basename(WAR)
# for line in list:
#     filepath = os.path.join(dir,line)
#     if os.path.isdir(filepath):
#         shutil.copyfile(WAR,filepath+'/'+BAOM)
#         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
# os.remove(WAR)
# logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
# return render_to_response('auto/auto-back.html',{'title':'autosso','aa':aa})    #chage
#
def zzbssso(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-sso.html',{'title':'zzbs'})  #chage

#def ssodep_33(req):
#       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/home/app/shell/sso.py')
#       ss = sun.split('\n')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/dep-bijia.html',{'title':'sso','ss':ss})
#
#def ssodep_34(req):
#       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/home/app/shell/sso.py')
#       ss = sun.split('\n')
#       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#       return render_to_response('auto/dep-bijia.html',{'title':'sso','ss':ss})


def ssodep_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py bijia /home/app/tomcat-7.0.27-message_notification-9680/ message_notification-9680 /nfsdata/bohan/sypt-super/sso/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


def ssohg_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py  bijia /home/app/tomcat-7.0.27-message_notification-9680/  message_notification-9680')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ssolog_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-message_notification-9680/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def ssodep_34(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py bijia /home/app/tomcat-7.0.27-message_notification-9680/ message_notification-9680 /nfsdata/bohan/sypt-super/sso/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ssohg_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py  bijia /home/app/tomcat-7.0.27-message_notification-9680/  message_notification-9680')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ssolog_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-message_notification-9680/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

#################################################################################################
@login_required
def registerlsjpassport(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_passport/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


def autolsjpassport(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/lsj_passport/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autolsjpassport','aa':aa})    #chage

def zzbslsjpassport(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbslsjpassport.html',{'title':'zzbs'})  #chage

def lsjpassportdep_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/home/app/shell/lsj_passport.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'lsjpassport','ss':ss})

def lsjpassportdep_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/home/app/shell/lsj_passport.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'lsjpassport','ss':ss})	   
################################################################################
@login_required
def registerchaoji99passport(req):   #chage
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/chaoji99_passport/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage


def autochaoji99passport(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/chaoji99_passport/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'autochaoji99passport','aa':aa})    #chage

def zzbschaoji99passport(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbschaoji99passport.html',{'title':'zzbs'})  #chage

def chaoji99passportdep_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/home/app/shell/chaoji99_passport.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'chaoji99passport','ss':ss})

def chaoji99passportdep_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/home/app/shell/chaoji99_passport.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'chaoji99passport','ss':ss})

@login_required
def registerlsjssodep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsjsso/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

def autolsj_sso(req):          #chage
 dir = u'/nfsdata/bohan/sypt-super/lsjsso/'         #chage
 auto = u'xxx'
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
# AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 aa = "tts_client is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/auto-back.html',{'title':'lsjsso','aa':aa})    #chage

def zzbslsjssodep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-lsjsso.html',{'title':'zzbs'})  #chage      
def lsjssodep_106(req):
       sun = ssh('192.168.3.106',58022,'bohan','sudo su - app','/home/app/shell/lsjsso.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdlsjssocs','ss':ss})

def autolizi(dir,auto):       
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 AUTOCONFIG= os.popen("/bin/autoconfig -u %s %s" % (auto,WAR)).read().strip('\n')
 os.popen("chmod -R 777 %s" % WAR).read().strip('\n')
 aa = AUTOCONFIG.split('\n')
 #logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return aa


def noautolizi(dir):     
 global WAR 
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 aa = "JAVA is not autoconfig, complete copy!!!"
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 #logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return aa


######################################################################################################
@login_required
def moldcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/mold/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/mold/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  
@login_required
def appcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/p4papp/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4papp/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})
@login_required
def engcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/p4peng/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4peng/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


def moldauto(req):
     aa = autolizi('/nfsdata/bohan/sypt-super/mold/','/home/app/auto_file/show/mold.properties')
    # logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
     return render_to_response('auto/auto.html',{'title':'www','aa':aa})

def appauto(req):
     aa = autolizi('/nfsdata/bohan/sypt-super/p4papp/','/home/app/auto_file/show/app.properties')
    # logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
     return render_to_response('auto/auto.html',{'title':'www','aa':aa})

def engauto(req):
     aa = autolizi('/nfsdata/bohan/sypt-super/p4peng/','/home/app/auto_file/show/engine.properties')
    # logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
     return render_to_response('auto/auto.html',{'title':'www','aa':aa})


def moldep_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def moldep_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def moldep_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def moldep_24(req):
       sun = ssh('192.168.3.24',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_24(req):
       sun = ssh('192.168.3.24',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_24(req):
       sun = ssh('192.168.3.24',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def moldep_25(req):
       sun = ssh('192.168.3.25',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_25(req):
       sun = ssh('192.168.3.25',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_25(req):
       sun = ssh('192.168.3.25',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def moldep_29(req):
       sun = ssh('192.168.3.29',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_29(req):
       sun = ssh('192.168.3.29',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_29(req):
       sun = ssh('192.168.3.29',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def moldep_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def moldep_8(req):
       sun = ssh('10.0.0.8',58022,'bohan','sudo su - app','/home/app/shell/mold/molddep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldhg_8(req):
       sun = ssh('10.0.0.8',58022,'bohan','sudo su - app','/home/app/shell/mold/moldhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def moldlog_8(req):
       sun = ssh('10.0.0.8',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-mold-8380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def appep_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def appep_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def appep_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def appep_68(req):
       sun = ssh('10.0.0.68',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_68(req):
       sun = ssh('10.0.0.68',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_68(req):
       sun = ssh('10.0.0.68',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def appep_85(req):
       sun = ssh('10.0.0.85',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_85(req):
       sun = ssh('10.0.0.85',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_85(req):
       sun = ssh('10.0.0.85',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/' )
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def appep_82(req):
       sun = ssh('192.168.3.82',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_82(req):
       sun = ssh('192.168.3.82',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_82(req):
       sun = ssh('192.168.3.82',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



def appep_97(req):
       sun = ssh('192.168.3.97',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def apphg_97(req):
       sun = ssh('192.168.3.97',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def applog_97(req):
       sun = ssh('192.168.3.97',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


#def appep_160(req):
#       sun = ssh('10.0.0.160',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def apphg_160(req):
#       sun = ssh('10.0.0.160',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def applog_160(req):
#       sun = ssh('10.0.0.160',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
#       ss = sun.split('\n')
#       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
#
#
#def appep_161(req):
#       sun = ssh('10.0.0.161',58022,'bohan','sudo su - app','/home/app/shell/app/appdep.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def apphg_161(req):
#       sun = ssh('10.0.0.161',58022,'bohan','sudo su - app','/home/app/shell/app/apphg.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def applog_161(req):
#       sun = ssh('10.0.0.161',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-app-8180/')
#       ss = sun.split('\n')
#       return render_to_response('auto/log.html',{'title':'tts','ss':ss})














def engdep_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_12(req):
       sun = ssh('192.168.3.12',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def engdep_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n') 
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def engdep_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n') 
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n') 
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

#def engdep_181(req):
#       sun = ssh('192.168.3.181',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def enghg_181(req):
#       sun = ssh('192.168.3.181',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def englog_181(req):
#       sun = ssh('192.168.3.181',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
#       ss = sun.split('\n')
#       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def engdep_85(req):
       sun = ssh('10.0.0.85',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_85(req):
       sun = ssh('10.0.0.85',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_85(req):
       sun = ssh('10.0.0.85',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def engdep_82(req):
       sun = ssh('192.168.3.82',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_82(req):
       sun = ssh('192.168.3.82',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_82(req):
       sun = ssh('192.168.3.82',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n') 
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def engdep_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name)) 
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def engdep_26(req):
       sun = ssh('192.168.3.26',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def enghg_26(req):
       sun = ssh('192.168.3.26',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def englog_26(req):
       sun = ssh('192.168.3.26',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

#def engdep_8(req):
#       sun = ssh('10.0.0.8',58022,'bohan','sudo su - app','/home/app/shell/eng/engdep.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def enghg_8(req):
#       sun = ssh('10.0.0.8',58022,'bohan','sudo su - app','/home/app/shell/eng/enghg.py')
#       ss = sun.split('\n')
#       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
#
#def englog_8(req):
#       sun = ssh('10.0.0.8',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-6.0.35-p4p-eng-8580/')
#       ss = sun.split('\n')
#       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



@login_required
def haolingzuicp(req):
    if req.method == 'POST':
        #os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_haolingzui/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_haolingzui/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


def haolingzuiauto(req):
     aa = noautolizi('/nfsdata/bohan/sypt-super/lsj_haolingzui/')
     #logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
     return render_to_response('auto/noauto.html',{'title':'www','aa':aa})
	 
	 
def haolingzuidep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/lsj_haolingzui.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def haolingzuihg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/lsj_haolingzuihg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def haolingzuilog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-lsj_haolingzui-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def haolingzuidep_44(req):
       sun = ssh('192.168.3.44',58022,'bohan','sudo su - app','/home/app/shell/lsj_haolingzui.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name)) 
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def haolingzuihg_44(req):
       sun = ssh('192.168.3.44',58022,'bohan','sudo su - app','/home/app/shell/lsj_haolingzuihg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def haolingzuilog_44(req):
       sun = ssh('192.168.3.44',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-lsj_haolingzui-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


#####################################
@login_required
def spcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/sp/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/sp/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})
	


def spdep_187(req):
       sun = ssh('10.0.0.187',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   

	   
def spdep_204(req):
       sun = ssh('10.0.0.204',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_225(req):
       sun = ssh('10.0.0.225',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_226(req):
       sun = ssh('10.0.0.226',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_227(req):
       sun = ssh('10.0.0.227',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_228(req):
       sun = ssh('10.0.0.228',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_229(req):
       sun = ssh('10.0.0.229',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_207(req):
       sun = ssh('10.0.0.207',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def spdep_190(req):
       sun = ssh('10.0.0.190',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	
def spdep_199(req):
       sun = ssh('10.0.0.199',58022,'bohan','sudo su - app','/home/app/shell/sp.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def registerqdhlz(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qdtts-haolingzui/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form}) 



def qdhlzmdep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/home/app/shell/tts-hlz.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdhlzmcs','ss':ss})
def qdhlzmdep_7(req):
       sun = ssh('10.0.0.7',58022,'bohan','sudo su - app','/home/app/rs-data.sh')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdhlzmcs','ss':ss})   
################################################################################################
class upForm(forms.Form):
    headImg  = forms.FileField()
@login_required
def regist(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/upload/*')
        uf = upForm(req.POST,req.FILES)
        if uf.is_valid():
            print uf.cleaned_data['headImg'].name
            print uf.cleaned_data['headImg'].size
            fp = file('/nfsdata/bohan/upload/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
           # return render_to_response('auto/dep-bijia.html',{'title':'tts'})
#            return HttpResponse('OK')
    else:
        uf = upForm()
    return render_to_response('regist.html',{'uf':uf})



def mlz_m_A13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','\cp /nfsdata/bohan/upload/* /home/app/nginx/html/haolingzui/activity/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})



@login_required
def registsb(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/upload/*')
        uf = upForm(req.POST,req.FILES)
        if uf.is_valid():
            fp = file('/nfsdata/bohan/uploadsb/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    else:
        uf = upForm()
    return render_to_response('registsb.html',{'uf':uf})



def mlz_sb_A13(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','\cp /nfsdata/bohan/uploadsb/* /home/app/nginx/html/bucai/extension/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


@login_required
def registbd(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/uploadbd/*')
        uf = upForm(req.POST,req.FILES)
        if uf.is_valid():
            fp = file('/nfsdata/bohan/uploadbd/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    else:
        uf = upForm()
    return render_to_response('auto/zzbs-qdbd.html',{'uf':uf})

def tts_bd_A13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','\cp /nfsdata/bohan/uploadbd/* /home/app/nginx/html/exts/browser-static/bd/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   

@login_required
def registbdtest(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/uploadbdtest/*')
        uf = upForm(req.POST,req.FILES)
        if uf.is_valid():
            fp = file('/nfsdata/bohan/uploadbdtest/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    else:
        uf = upForm()
    return render_to_response('auto/zzbs-qdbdtest.html',{'uf':uf})

def tts_bd_A13test(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','\cp /nfsdata/bohan/uploadbdtest/* /home/app/nginx/html/exts/browser-static/bdtest/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})



#############################################################################################
@login_required
def hlz_seckillcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_seckill/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_seckill/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_seckilldep_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/home/app/shell/hlz_seckill.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_seckillhg_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/home/app/shell/hlz_seckillhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_seckilllog_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_seckill-8480/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_seckilldep_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/home/app/shell/hlz_seckill.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_seckillhg_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/home/app/shell/hlz_seckillhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_seckilllog_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_seckill-8480/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def hlz_tradecp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_trade/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_trade/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_tradedep_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/home/app/shell/hlz_trade.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_tradehg_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/home/app/shell/hlz_tradehg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_tradelog_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_trade_web-6280/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_tradedep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_trade.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_tradehg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_tradehg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_tradelog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_trade_web-6280/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def hlz_cmsproxycp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_cmsproxy/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_cmsproxy/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_cmsproxydep_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxy.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxyhg_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxyhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxylog_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_cmsproxy-8380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_cmsproxydep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxy.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxyhg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxyhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxylog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_cmsproxy-8380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def hlz_cmsproxydep_19(req):
       sun = ssh('192.168.3.19',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxy.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxyhg_19(req):
       sun = ssh('192.168.3.19',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxyhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxylog_19(req):
       sun = ssh('192.168.3.19',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_cmsproxy-8380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def hlz_cmsproxydep_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxy.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxyhg_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmsproxyhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmsproxylog_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_cmsproxy-8380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def hlz_paycp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_pay/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_pay/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})



def hlz_paydep_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_pay.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_payhg_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_payhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_paylog_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_payweb-6380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_paydep_46(req):
       sun = ssh('192.168.3.46',58022,'bohan','sudo su - app','/home/app/shell/hlz_pay.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_payhg_46(req):
       sun = ssh('192.168.3.46',58022,'bohan','sudo su - app','/home/app/shell/hlz_payhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_paylog_46(req):
       sun = ssh('192.168.3.46',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_payweb-6380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required   
def hlz_passportcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_passport/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_passport/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_passportdep_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_passport.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_passporthg_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_passporthg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_passportlog_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_passport-8780/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_passportdep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_passport.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_passporthg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_passporthg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_passportlog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_passport-8780/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def hlz_sellercp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_seller/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_seller/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#def hlz_sellerauto(req):
#     aa = noautolizi('/nfsdata/bohan/sypt-super/lsj_hlz_seller/')
#     return render_to_response('auto/noauto.html',{'title':'www','aa':aa})


def hlz_sellerdep_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_seller.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_sellerhg_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_sellerhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_sellerlog_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','' % t)
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_sellerdep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_seller.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_sellerhg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_sellerhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_sellerlog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py   /home/app/tomcat-7.0.27-hlz_seller-8980/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})







def hlz_sellerdep_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/home/app/shell/hlz_seller.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_sellerhg_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/home/app/shell/hlz_sellerhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_sellerlog_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py   /home/app/tomcat-7.0.27-hlz_seller-8980/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})






@login_required
def hlz_cmscp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_cms/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_cms/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#def hlz_cmsauto(req):
#     aa = noautolizi('/nfsdata/bohan/sypt-super/lsj_hlz_cms/')
#     return render_to_response('auto/noauto.html',{'title':'www','aa':aa})


def hlz_cmsdep_106(req):
       sun = ssh('192.168.3.106',58022,'bohan','sudo su - app','/home/app/shell/hlz_cms.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmshg_106(req):
       sun = ssh('192.168.3.106',58022,'bohan','sudo su - app','/home/app/shell/hlz_cmshg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_cmslog_106(req):
       sun = ssh('192.168.3.106',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_cms-9480/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def hlz_mcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/lsj_hlz_m/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/lsj_hlz_m/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


#def hlz_mauto(req):
#     aa = noautolizi('/nfsdata/bohan/sypt-super/lsj_hlz_m/')
#     return render_to_response('auto/noauto.html',{'title':'www','aa':aa})


def hlz_mdep_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_m.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_mhg_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/home/app/shell/hlz_mhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_mlog_64(req):
       sun = ssh('192.168.3.64',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_m-8680/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def hlz_mdep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_m.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_mhg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_mhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_mlog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_m-8680/ ')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def qly_plugincp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qly_plugin/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_plugin/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




@login_required
def qly_plugindep_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_plugin /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480 /nfsdata/bohan/sypt-super/qly_plugin/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginhg_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginlog_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_plugin-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginrestart_32(req):
       sun = ssh('192.168.3.32',58022,'bohan','sudo su - app','~/shell/restart.sh qly_plugin 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

	   
@login_required	   
def qly_plugindep_36(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_plugin /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480 /nfsdata/bohan/sypt-super/qly_plugin/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginhg_36(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginlog_36(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-qly_plugin-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginrestart_36(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','~/shell/restart.sh qly_plugin 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def qly_plugindep_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_plugin /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480 /nfsdata/bohan/sypt-super/qly_plugin/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginhg_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginlog_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-qly_plugin-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginrestart_80(req):
       sun = ssh('192.168.3.80',58022,'bohan','sudo su - app','~/shell/restart.sh qly_plugin 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def qly_plugindep_23(req):
       sun = ssh('192.168.3.101',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_plugin /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480 /nfsdata/bohan/sypt-super/qly_plugin/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginhg_23(req):
       sun = ssh('192.168.3.101',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_plugin-8480/ qly_plugin-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginlog_23(req):
       sun = ssh('192.168.3.101',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-qly_plugin-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def qly_pluginrestart_23(req):
       sun = ssh('192.168.3.101',58022,'bohan','sudo su - app','~/shell/restart.sh qly_plugin 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def hlz_lotterycp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/hlz_lottery/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/hlz_lottery/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def hlz_lotterydep_17(req):
       sun = ssh('192.168.3.17',58022,'bohan','sudo su - app','/home/app/shell/hlz_lottery.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_lotteryhg_17(req):
       sun = ssh('192.168.3.17',58022,'bohan','sudo su - app','/home/app/shell/hlz_lotteryhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_lotterylog_17(req):
       sun = ssh('192.168.3.17',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_lottery-8380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def hlz_lotterydep_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/home/app/shell/hlz_lottery.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_lotteryhg_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/home/app/shell/hlz_lotteryhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_lotterylog_18(req):
       sun = ssh('192.168.3.18',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_lottery-8380/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
	   
@login_required
def brcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/br/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/br/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

@login_required
def brdep1_183(req):
       sun = ssh('10.0.0.183',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  browser  /home/app/tts-browser-plugin    /nfsdata/bohan/sypt-super/br/*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def bjrestart_183(req):
       sun = ssh('10.0.0.183',58022,'bohan','sudo su - app','/home/app/shell/bjrestart.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	
@login_required  
def brdep1_94(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  browser  /home/app/tts-browser-plugin    /nfsdata/bohan/sypt-super/br/*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def bjrestart_94(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','/home/app/shell/bjrestart.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


@login_required
def brdep1_83(req):
       sun = ssh('192.168.3.83',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  browser  /home/app/tts-browser-plugin    /nfsdata/bohan/sypt-super/br/*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def bjrestart_83(req):
       sun = ssh('192.168.3.83',58022,'bohan','sudo su - app','/home/app/shell/bjrestart.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


@login_required
def brdep1_48(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  browser  /home/app/tts-browser-plugin    /nfsdata/bohan/sypt-super/br/*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def bjrestart_48(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','/home/app/shell/bjrestart.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

@login_required
def brdep1_51(req):
       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  browser  /home/app/tts-browser-plugin    /nfsdata/bohan/sypt-super/br/*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def bjrestart_51(req):
       sun = ssh('10.0.0.51',58022,'bohan','sudo su - app','/home/app/shell/bjrestart.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_bbscp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qlybbs/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qlybbs/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})



@login_required
def qly_bbsdep_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','/home/app/shell/qly_bbs.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_bbshg_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','/home/app/shell/qly_bbshg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

@login_required
def qly_bbslog_39(req):
       sun = ssh('192.168.3.39',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_bbs-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def qly_bbsdep_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','/home/app/shell/qly_bbs.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_bbshg_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','/home/app/shell/qly_bbshg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def qly_bbslog_40(req):
       sun = ssh('192.168.3.40',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_bbs-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def p4p_ipcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/p4pip/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4pip/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})



@login_required
def p4p_ipdep_48(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','/home/app/shell/p4p_ip.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def p4p_iphg_48(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','/home/app/shell/p4p_iphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def p4p_iplog_48(req):
       sun = ssh('10.0.0.48',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-p4p_ip-7180/' )
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def p4p_ipdep_94(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','/home/app/shell/p4p_ip.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def p4p_iphg_94(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','/home/app/shell/p4p_iphg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def p4p_iplog_94(req):
       sun = ssh('192.168.3.94',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-p4p_ip-7180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def registerwylmdep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/wylm/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
@login_required
def wylm_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/ext/ext_wylm.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextcs','ss':ss})
@login_required
def cdn_wylm_post(req):
       ss = do_post1("http://ext.taotaosou.com/wylm/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})
@login_required
def registerwylmsdep(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/exts_wylm/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

def wylms_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/exts/exts_wylm.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextcs','ss':ss})
@login_required
def hlz_scorecp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/hlz_score/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/hlz_score/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_scoredep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_score.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_scorehg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_scorehg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_scorelog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_score-8580/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def hlz_scoredep_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/home/app/shell/hlz_score.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_scorehg_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/home/app/shell/hlz_scorehg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_scorelog_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py   /home/app/tomcat-7.0.27-hlz_score-8580/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def hlz_rewardcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/hlz_reward/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/hlz_reward/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_rewarddep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_reward.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_rewardhg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_rewardhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_rewardlog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_reward-8680/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def hlz_rewarddep_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/home/app/shell/hlz_reward.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_rewardhg_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/home/app/shell/hlz_rewardhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_rewardlog_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-hlz_reward-8680/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def registeruniondep(req):
    if req.method == 'POST':
	os.system('rm -rf /nfsdata/bohan/sypt-super/qianduan/union/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/union/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  

def union_13(req):
       sun = ssh('10.0.0.13',58022,'bohan','sudo su - app','/home/app/shell/union.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'union','ss':ss})

@login_required
def p4p_pubcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/p4p_pub/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/p4p_pub/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def p4p_pubdep_81(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','/home/app/shell/p4p_pub.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def p4p_pubhg_41(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','/home/app/shell/p4p_pubhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def p4p_publog_41(req):
       sun = ssh('192.168.3.81',58022,'bohan','sudo su - app','tail -n 200 /home/app/tomcat-8.0.23-pub-8580/logs/catalina.out')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
	   
@login_required
def hlz_mqcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/hlz_mq/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/hlz_mq/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




def hlz_mqdep_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_mq.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_mqhg_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/home/app/shell/hlz_mqhg.py')
       ss = sun.split('\n')
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def hlz_mqlog_91(req):
       sun = ssh('10.0.0.91',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-hlz_mq-8180/')
       ss = sun.split('\n')
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def register_qly_extension(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qly_extension/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage

def qly_extension_164(req):
       sun = ssh('10.0.0.164',58022,'bohan','sudo su - app','/home/app/shell/qly_extension.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdextscs','ss':ss})

@login_required
def registertts_addep(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qianduan/tts_ad/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/tts_ad/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def tts_ad_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/home/app/shell/tts-ad.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts_ad','ss':ss})

def cdn_tts_ad_post(req):
       ss = do_post("http://img.taotaosou.cn/tts-ad/","http://img01.taotaosou.cn/tts-ad/","http://img02.taotaosou.cn/tts-ad/","http://img03.taotaosou.cn/tts-ad/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})
@login_required
def registerad_mgrcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/ad_mgr/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/ad_mgr/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def ad_mgrdep_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/home/app/shell/ad_mgr.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ad_mgrhg_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/home/app/shell/ad_mgrhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ad_mgrlog_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-ad-mgr-6380/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

def ad_mgrrestart_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','~/shell/restart.sh ad-mgr  6380 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def ad_promotioncp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/ad-promotion/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/ad-promotion/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})



def ad_promotiondep_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/home/app/shell/ad-promotion.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ad_promotionhg_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/home/app/shell/ad-promotionhg.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def ad_promotionlog_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-ad-promotion-6480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def salecp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/sale/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/sale/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})


def saledep1_36(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','/home/app/shell/tts-sale.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
def saledep1_37(req):
       sun = ssh('192.168.3.37',58022,'bohan','sudo su - app','/home/app/shell/tts-sale.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

@login_required
def sale_admincp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/tts-sale-admin/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/tts-sale-admin/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def sale_admindep1_36(req):
       sun = ssh('192.168.3.36',58022,'bohan','sudo su - app','/home/app/shell/sale-admin.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
@login_required
def registerqly_findhuo(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qly_findhuo/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/findhuo/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage
	
	
	
def zzbsqly_findhuo(req):                    #chage
 logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
 return render_to_response('auto/zzbs-qly_findhuo.html',{'title':'zzbs'})  #chage

def qly_findhuodep_42(req):
       sun = ssh('192.168.3.42',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  qly_findhuo /home/app/tts-supply-plugin /nfsdata/bohan/sypt-super/findhuo/tts-supply-plugin-*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly_findhuo','ss':ss})

def qly_findhuodep_49(req):
       sun = ssh('192.168.3.49',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py   qly_findhuo /home/app/tts-supply-plugin /nfsdata/bohan/sypt-super/findhuo/tts-supply-plugin-*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly_findhuo','ss':ss})

#@login_required
#def CHECKIP(req):
#    IP = ['10.0.0.32','192.168.3.194','10.0.0.95','192.168.3.195','10.0.0.75','10.0.0.96','10.0.0.97','10.0.0.89','10.0.0.166','10.0.0.98','192.168.3.190','192.168.3.199','10.0.0.93','192.168.3.191','192.168.3.197','192.168.3.198','192.168.3.193','192.168.3.192','10.0.0.90','192.168.3.95','192.168.3.112','10.0.0.189','10.0.0.168','192.168.3.135','192.168.3.113','192.168.3.137','192.168.3.111','10.0.0.200','10.0.0.170']
#    if req.method == 'POST':
#        form = UserForm(req.POST)
#        if form.is_valid():
#            DD = form.cleaned_data
#            PP = DD['name']
#            sun = ssh(PP,58022,'bohan','sudo su - app','dstat -cdln 1 5')
#            ss = sun.split('\n')
#            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
#            return render_to_response('checklog.html',{'title':'tts','ss':ss,'PP':PP})
#    else:
#        form = UserForm()
#    return render_to_response('checkregister.html',{'form':form,'IP':IP})
#

def CHECKIP(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            PP = DD['name']
            sun = ssh(PP,58022,'bohan','sudo su - app','dstat -cdln 1 5')
            ss = sun.split('\n')
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
            return render_to_response('checkregister.html',{'title':'tts','ss':ss,'PP':PP})
    else:
        form = UserForm()
    return render_to_response('checkregister.html',{'form':form})

###########################################################################
@login_required
def registerqdfindhuodep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/findhuo/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/findhuo/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



def zzbsqdfindhuodep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-qdfindhuo.html',{'title':'zzbs'})  #chage      
def qdqdfindhuodep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  findhuo /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/findhuo/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdqdfindhuocs','ss':ss})
def cdn_qdfindhuo_post(req):
       ss = do_post("http://img.taotaosou.cn/findhuo/","http://img01.taotaosou.cn/findhuo/","http://img02.taotaosou.cn/findhuo/","http://img03.taotaosou.cn/findhuo/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})

@login_required
def registerqdtkdep(req):
    if req.method == 'POST':
	os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/tk/tk*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/tk/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage



def zzbsqdtkdep(req):                    #chage
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/zzbs-qdtk.html',{'title':'zzbs'})  #chage      
def qdtkdep_164(req):
       sun = ssh('10.0.0.164',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  tk /home/app/nginx/html/  /nfsdata/bohan/sypt-super/qianduan/tk/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdtkcs','ss':ss})
def cdn_qdtk_post(req):
       ss = do_post1("http://tk.taotaosou.com/")
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/cdn.html',{'title':'cdn','ss':ss})
@login_required
def SIP(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                sun = ssh1(PP,58022,'bohan','sudo su - root','/home/app/shell/hard_check.py')
                ss = sun.split('\n')
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return render_to_response('auto/dep-bijia.html',{'ss':ss})
            except :
                return HttpResponse('IP input error')

    else:
        form = UserForm()
    return render_to_response('re.html',{'form':form})

@login_required
def qly_moneycp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qly_money/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_money/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def qly_moneydep_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_money /home/app/tomcat-7.0.27-qly_money-8480/ qly_money-8480 /nfsdata/bohan/sypt-super/qly_money/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_moneyhg_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_money-8480/ qly_money-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_moneylog_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_money-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})




def qly_moneydep_25(req):
       sun = ssh('192.168.3.25',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_money /home/app/tomcat-7.0.27-qly_money-8480/ qly_money-8480 /nfsdata/bohan/sypt-super/qly_money/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_moneyhg_25(req):
       sun = ssh('192.168.3.25',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_money-8480/ qly_money-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_moneylog_25(req):
       sun = ssh('192.168.3.25',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py  /home/app/tomcat-7.0.27-qly_money-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def registerqdsjddep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/sjd/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/sjd/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close() 
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  



def qdqdsjddep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  tts-sjd /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/sjd/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdqdsjdcs','ss':ss})
@login_required
def qly_weixincp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qly_weixin/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_weixin/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def qly_weixindep_149(req):
       sun = ssh('192.168.3.149',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_weixin /home/app/tomcat-7.0.27-tts_weixin-8080/ tts_weixin-8080 /nfsdata/bohan/sypt-super/qly_weixin/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_weixinhg_149(req):
       sun = ssh('192.168.3.149',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-tts_weixin-8080/  tts_weixin-8080')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_weixinlog_149(req):
       sun = ssh('192.168.3.149',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-tts_weixin-8080/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


@login_required
def qly_datacp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qly_data/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_data/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def qly_datadep_109(req):
       sun = ssh('10.0.0.109',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_data /home/app/tomcat-7.0.27-qly_data-6180/ qly_data-6180 /nfsdata/bohan/sypt-super/qly_data/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datahg_109(req):
       sun = ssh('10.0.0.109',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_data-6180/  qly_data-6180')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datalog_109(req):
       sun = ssh('10.0.0.109',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_data-6180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



def qly_datadep_122(req):
       sun = ssh('10.0.0.122',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_data /home/app/tomcat-7.0.27-qly_data-6180/ qly_data-6180 /nfsdata/bohan/sypt-super/qly_data/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datahg_122(req):
       sun = ssh('10.0.0.122',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_data-6180/  qly_data-6180')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datalog_122(req):
       sun = ssh('10.0.0.122',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_data-6180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
	   
	   
def qly_datadep_29(req):
       sun = ssh('10.0.0.29',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_data /home/app/tomcat-7.0.27-qly_data-6180/ qly_data-6180 /nfsdata/bohan/sypt-super/qly_data/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datahg_29(req):
       sun = ssh('10.0.0.29',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_data-6180/  qly_data-6180')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datalog_29(req):
       sun = ssh('10.0.0.29',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_data-6180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
	   
def qly_datadep_143(req):
       sun = ssh('10.0.0.143',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_data /home/app/tomcat-7.0.27-qly_data-6180/ qly_data-6180 /nfsdata/bohan/sypt-super/qly_data/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datahg_143(req):
       sun = ssh('10.0.0.143',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_data-6180/  qly_data-6180')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_datalog_143(req):
       sun = ssh('10.0.0.143',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_data-6180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
@login_required
def registextend(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/uploadextend/*')
        uf = upForm(req.POST,req.FILES)
        if uf.is_valid():
            fp = file('/nfsdata/bohan/uploadextend/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
    else:
        uf = upForm()
    logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    return render_to_response('auto/zzbs-qdextend.html',{'uf':uf})

def tts_extend_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','\cp /nfsdata/bohan/uploadextend/* /home/app/data/tts/extension-qly/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   
@login_required
def registerqdcrmdep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/crm/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/crm/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def qdqdcrmdep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  tts-crm /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/crm/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdqdcrmcs','ss':ss})


@login_required
def qly_scorecp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qly_score/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_score/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def qly_scoredep_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_score /home/app/tomcat-7.0.27-qly_score-6180/ qly_score-6180 /nfsdata/bohan/sypt-super/qly_score/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_scorehg_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_score-6180/  qly_data-6180')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_scorelog_33(req):
       sun = ssh('192.168.3.33',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_score-6180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



def qly_scoredep_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_score /home/app/tomcat-7.0.27-qly_score-6180/ qly_score-6180 /nfsdata/bohan/sypt-super/qly_score/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_scorehg_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_score-6180/  qly_data-6180')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_scorelog_34(req):
       sun = ssh('192.168.3.34',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_score-6180/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



@login_required
def registsb(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/songbo/*')
        uf = upForm(req.POST,req.FILES)
        if uf.is_valid():
            fp = file('/nfsdata/bohan/songbo/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    else:
        uf = upForm()
    return render_to_response('auto/zzbs-qdsb.html',{'uf':uf})

def tts_sb_203(req):
       sun = ssh('10.0.0.203',58022,'bohan','sudo su - murphy','/home/murphy/shell/html.py')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


def registwydown(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/wy_download/*')
        uf = upForm(req.POST, req.FILES)
        if uf.is_valid():
            fp = file('/nfsdata/bohan/wy_download/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
    else:
        uf = upForm()
    return render_to_response('auto/zzbs-wydown.html',{'uf':uf})

def tts_wydown_86(req):
    sun = ssh('10.0.0.86', 58022, 'bohan', 'sudo su - app', '\cp /nfsdata/bohan/wy_download/*  /home/app/data/tts/wy_download/')
    ss = sun.split('\n')
    logger.info('当用户:-%s-,执行函数名:%s ' % (req.user, sys._getframe().f_code.co_name))
    return render_to_response('auto/dep-bijia.html', {'title': 'tts_ad', 'ss': ss})


@login_required
def weiyousb(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        BB = req.POST['b1']
        CC = req.POST['c1']
        DD = req.POST['ssql']
        #zk = zookeeper.init("199.155.122.131:2181")
        zk=zookeeper.init("10.0.0.225:2181,10.0.0.226:2181,10.0.0.227:2181,10.0.0.228:2181,10.0.0.229:2181")
        a = {"v1": AA, "v2": BB, "v3": CC}
        zookeeper.set(zk,"/taotaosou/fabu",json.dumps(a))
        now = datetime.datetime.now()
        p2 = WYLOG(time=now,deploy='微友', message='%s'%DD)
        p2.save()
        logger.info('当用户:-%s-,执行函数名:%s ' % (req.user, sys._getframe().f_code.co_name))
        return render_to_response('weiyousb.html',{'ss':'Upload complete'})
    else:
        return render_to_response('weiyousb.html')


@login_required
def weiyousbtest(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        BB = req.POST['b1']
        CC = req.POST['c1']
        a = {"v1": AA, "v2": BB, "v3": CC}
        zk = zookeeper.init("199.155.122.131:2181")
        zookeeper.set(zk,"/taotaosou/fabu",json.dumps(a))
        zk1 = zookeeper.init("199.155.122.233:2181")
        zookeeper.set(zk1,"/taotaosou/fabu",json.dumps(a))  
        logger.info('当用户:-%s-,执行函数名:%s ' % (req.user, sys._getframe().f_code.co_name))
        return render_to_response('weiyousbtest.html',{'ss':'Upload complete'})
      #  return render_to_response('weiyousbtest.html',{'ss':AA+BB+CC})
    else:
        return render_to_response('weiyousbtest.html')


@login_required
def qly_screencp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qly_screen/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_screen/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def qly_screendep_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly_screen /home/app/tomcat-7.0.27-qly_screen-8680/ qly_screen-8680 /nfsdata/bohan/sypt-super/qly_screen/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_screenhg_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qly /home/app/tomcat-7.0.27-qly_screen-8680/  qly_data-8680')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qly_screenlog_23(req):
       sun = ssh('192.168.3.23',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_screen-8680/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


@login_required
def wy_wwwcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/wy_www/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/wy_www/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




@login_required
def wywwwlog(req):
    if req.method == 'POST':
        S1 = req.POST['S1']
        S2 = req.POST['S2']
        sun = ssh('%s'%S2,58022,'bohan','sudo su - app','tail -n 500 weiyou-web-[0-9].[0-9].[0-9]/logs/%s'%S1)
        ss = sun.split('\n')
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/log.html',{'title':'tts','ss':ss})
    else:
        return render_to_response('auto/zzbs-wy_www.html')

def wy_wwwdep_65(req):
       sun = ssh('192.168.3.65',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/wy.py   /home/app  weiyou-web /nfsdata/bohan/sypt-super/wy_www')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


def wy_wwwdep_72(req):
       sun = ssh('192.168.3.72',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/wy.py   /home/app  weiyou-web /nfsdata/bohan/sypt-super/wy_www')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


@login_required
def socketcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/wy_socket/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/wy_socket/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})




@login_required
def wysocketlog(req):
    if req.method == 'POST':
        S1 = req.POST['S1']
        S2 = req.POST['S2']
        sun = ssh('%s'%S2,58022,'bohan','sudo su - app','tail -n 500 weiyou-socket-server-[0-9].[0-9].[0-9]/logs/%s'%S1)
        ss = sun.split('\n')
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/log.html',{'title':'tts','ss':ss})
    else:
        return render_to_response('auto/zzbs-socket.html')


def socketdep_68(req):
       sun = ssh('192.168.3.68',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/wysocket.py    /home/app  weiyou-socket-server /nfsdata/bohan/sypt-super/wy_socket 115.236.185.104')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def socketdep_74(req):
       sun = ssh('192.168.3.74',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/wysocket.py    /home/app  weiyou-socket-server /nfsdata/bohan/sypt-super/wy_socket 115.236.185.106')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def socketyz(req):
       zk=zookeeper.init("10.0.0.225:2181,10.0.0.226:2181,10.0.0.227:2181,10.0.0.228:2181,10.0.0.229:2181")
       ss=zookeeper.get_children(zk,"/taotaosou/weiyou/socket",None)
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss}) 

@login_required
def wy_pubcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/wy_pub/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/wy_pub/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

@login_required
def wy_publog(req):
    if req.method == 'POST':
        S1 = req.POST['S1']
        S2 = req.POST['S2']
        sun = ssh('%s'%S2,58022,'bohan','sudo su - app','tail -n 500 weiyou-weixin-pub-[0-9].[0-9].[0-9]/logs/%s'%S1)
        ss = sun.split('\n')
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/log.html',{'title':'tts','ss':ss})
    else:
        return render_to_response('auto/zzbs-wy_pub.html')

def wy_pubdep_63(req):
       sun = ssh('192.168.3.63',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/wy.py   /home/app weiyou-weixin-pub /nfsdata/bohan/sypt-super/wy_pub')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


def wy_pubdep_71(req):
       sun = ssh('192.168.3.71',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/wy.py   /home/app  weiyou-weixin-pub /nfsdata/bohan/sypt-super/wy_pub')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})


@login_required
def wy_backcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/wy_back/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/wy_back/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def wy_backdep_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py weiyou /home/app/tomcat-7.0.27-weiyou_back-6680/ weiyou_back-6680 /nfsdata/bohan/sypt-super/wy_back/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def wy_backhg_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py weiyou /home/app/tomcat-7.0.27-weiyou_back-6680/ weiyou_back-6680')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def wy_backlog_124(req):
       sun = ssh('192.168.3.124',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-weiyou_back-6680/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
	   

@login_required
def spider149cp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/spdiertmp/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/spdiertmp/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                os.system('echo %s > /tmp/spdier.tmp'%cc )
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK,%s' % (remotepath,localpath,cc))
            except Exception, e:
                return HttpResponse('path error %s'%e)
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

@login_required
def spider149(req):
      context = os.popen('cat /tmp/spdier.tmp').read().strip()
      ssh1('192.168.3.149',58022,'bohan','sudo su - root','rm -rf /home/app/srv/salt/base/init/files/spdiertmp/*.zip && \cp /nfsdata/bohan/sypt-super/spdiertmp/%s /home/app/srv/salt/base/init/files/spdiertmp/'%context)
      sun = ssh1('192.168.3.149',58022,'bohan','sudo su - root','salt -L "10.0.0.55,10.0.0.56,10.0.0.57,10.0.0.137,10.0.0.138,10.0.0.66,10.0.0.67,10.0.0.68,10.0.0.69,10.0.0.70,10.0.0.103,10.0.0.104,10.0.0.105,10.0.0.106,10.0.0.117,10.0.0.107,10.0.0.108,10.0.0.111,192.168.4.60,192.168.4.61,192.168.4.62,192.168.4.63,192.168.4.64,192.168.4.65" cp.get_file salt://init/files/spdiertmp/%s  /tmp/%s  runas="webman"'%(context,context))
      strinfo = re.compile('\[\d+m')
      b = strinfo.sub('',sun)
      strinfo = re.compile('\[\d+;\d+m')
      ss = strinfo.sub(' ',b)
      ss = ss.split('\n')
      print ss
      return render_to_response('auto/dep-bijia.html', {'title': 'tts_ad', 'ss': ss})

@login_required
def spider149dep(req):
      context = os.popen('cat /tmp/spdier.tmp').read().strip()
      sun = ssh1('192.168.3.149',58022,'bohan','sudo su - root','salt -L "10.0.0.55,10.0.0.56,10.0.0.57,10.0.0.137,10.0.0.138,10.0.0.66,10.0.0.67,10.0.0.68,10.0.0.69,10.0.0.70,10.0.0.103,10.0.0.104,10.0.0.105,10.0.0.106,10.0.0.117,10.0.0.107,10.0.0.108,10.0.0.111,192.168.4.60,192.168.4.61,192.168.4.62,192.168.4.63,192.168.4.64,192.168.4.65" cmd.run "/home/webman/shell/spider.py /home/webman/aliyun-downloader aliyun-downloader /tmp/"  runas="webman"')
      ssh1('192.168.3.149',58022,'bohan','sudo su - root','salt -L "10.0.0.55,10.0.0.56,10.0.0.57,10.0.0.137,10.0.0.138,10.0.0.66,10.0.0.67,10.0.0.68,10.0.0.69,10.0.0.70,10.0.0.103,10.0.0.104,10.0.0.105,10.0.0.106,10.0.0.117,10.0.0.107,10.0.0.108,10.0.0.111,192.168.4.60,192.168.4.61,192.168.4.62,192.168.4.63,192.168.4.64,192.168.4.65" cmd.run "rm -rf /tmp/*.zip"')
      strinfo = re.compile('\[\d+m')
      b = strinfo.sub('',sun)
      strinfo = re.compile('\[\d+;\d+m')
      ss = strinfo.sub(' ',b)
      ss = ss.split('\n')
      print ss
      return render_to_response('auto/dep-bijia.html', {'title': 'tts_ad', 'ss': ss})






@login_required
def spider149log(req):
    #QQ = ('10.0.0.55','10.0.0.56','10.0.0.57','10.0.0.137','10.0.0.138','10.0.0.66','10.0.0.67','10.0.0.68','10.0.0.69','10.0.0.70','10.0.0.103','10.0.0.104','10.0.0.105','10.0.0.106','10.0.0.117','10.0.0.107','10.0.0.108','10.0.0.111')
    QQ = ('10.0.0.55','10.0.0.56','10.0.0.57','10.0.0.137','10.0.0.138','10.0.0.66','10.0.0.67','10.0.0.68','10.0.0.69','10.0.0.70','10.0.0.103','10.0.0.104','10.0.0.105','10.0.0.106','10.0.0.117','10.0.0.107','10.0.0.108','10.0.0.111','192.168.4.60','192.168.4.61','192.168.4.62','192.168.4.63','192.168.4.64','192.168.4.65')
    if req.method == 'POST':
        AA = req.POST['a1']
        sun = ssh('%s'%AA,58022,'bohan','sudo su - webman','tail -n 200 /home/webman/aliyun-downloader/aliyun-downloader-*/logs/downloader-biz.log')
        ss = sun.split('\n') 
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/log.html',{'ss':ss})
    else:
        return render_to_response('auto/zzbs-spider.html',{'QQ':QQ})



@login_required
def androiddl(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        ssh('10.0.0.164',58022,'bohan','sudo su - app','echo "%s" > /home/app/nginx/html/androiddl.html'%AA)
        ss = os.popen('curl androiddl.weiyoucrm.com').read().strip()
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/zzbs-androiddl.html',{'ss':'通过获取当前网页信息，得到版本号为:%s'%ss})
    else:
        return render_to_response('auto/zzbs-androiddl.html')


@login_required
def extend(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        ssh('10.0.0.164',58022,'bohan','sudo su - app','echo "%s" > /home/app/nginx/html/extend.html'%AA)
        ss = os.popen('curl extend.weiyoucrm.com').read().strip()
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/zzbs-extend.html',{'ss':'通过获取当前网页信息，得到版本号为:%s'%ss})
    else:
        return render_to_response('auto/zzbs-extend.html')


@login_required
def opinioncp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/opinion/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/opinion/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})



def opiniondep_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py opinion /home/app/tomcat-8.0.15-opinion-6280/ opinion-6280 /nfsdata/bohan/sypt-super/opinion/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def opinionhg_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py opinion /home/app/tomcat-8.0.15-opinion-6280/  opinion-6280')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def opinionlog_13(req):
       sun = ssh('192.168.3.13',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-opinion-6280/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})	   



@login_required
def opbackcp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/opback/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/opback/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def opbackdep_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py opback /home/app/tomcat-8.0.15-opinion_back-6280/ opinion_back-6280 /nfsdata/bohan/sypt-super/opback/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})
	   



def opbackhg_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py opback /home/app/tomcat-8.0.15-opinion_back-6280/  opinion_back-6280')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def opbacklog_14(req):
       sun = ssh('192.168.3.14',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-opinion_back-6280/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



@login_required
def qlymanagercp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/qlymanager/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qlymanager/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def qlymanagerdep_50(req):
       sun = ssh('192.168.4.50',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly /home/app/tomcat-7.0.27-qly_manager-8480/ qly_manager-8480 /nfsdata/bohan/sypt-super/qlymanager/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qlymanagerhg_50(req):
       sun = ssh('192.168.4.50',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qlymanager /home/app/tomcat-7.0.27-qly_manager-8480/  qly_manager-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qlymanagerlog_50(req):
       sun = ssh('192.168.4.50',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_manager-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def qly_restart_50(req):
       sun = ssh('192.168.4.50',58022,'bohan','sudo su - app','~/shell/restart.sh qly_manager 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


def qlymanagerdep_51(req):
       sun = ssh('192.168.4.51',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs.py qly /home/app/tomcat-7.0.27-qly_manager-8480/ qly_manager-8480 /nfsdata/bohan/sypt-super/qlymanager/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qlymanagerhg_51(req):
       sun = ssh('192.168.4.51',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py qlymanager /home/app/tomcat-7.0.27-qly_manager-8480/  qly_manager-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def qlymanagerlog_51(req):
       sun = ssh('192.168.4.51',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-7.0.27-qly_manager-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def qly_restart_51(req):
       sun = ssh('192.168.4.51',58022,'bohan','sudo su - app','~/shell/restart.sh qly_manager 8480 restart')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})


@login_required
def registeryunkefudep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/yunkefu/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/yunkefu/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def qdyunkefudep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  yunkefu /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/yunkefu/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdyunkefucs','ss':ss})


@login_required
def weidiandqtest(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        BB = req.POST['b1']
        CC = req.POST['c1']
        url = "http://199.155.122.116:8022/syncIndex.do?v1=%s&v2=%s&v3=%s"%(AA,BB,CC)
        conn = httplib.HTTPConnection("199.155.122.116:8022")
        conn.request(method="GET", url=url)
        response = conn.getresponse()
        res = response.read()
        logger.info('当用户:-%s-,执行函数名:%s ' % (req.user, sys._getframe().f_code.co_name))
        return render_to_response('weidiandqtest.html',{'ss': res})
    else:
        return render_to_response('weidiandqtest.html')

@login_required
def weidiandq(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        BB = req.POST['b1']
        CC = req.POST['c1']
        url = "http://mall.taotaosou.com/syncIndex.do?v1=%s&v2=%s&v3=%s"%(AA,BB,CC)
        conn = httplib.HTTPConnection("mall.taotaosou.com")
        conn.request(method="GET", url=url)
        response = conn.getresponse()
        res = response.read()
        logger.info('当用户:-%s-,执行函数名:%s ' % (req.user, sys._getframe().f_code.co_name))
        return render_to_response('weidiandq.html',{'ss': res})
    else:
        return render_to_response('weidiandq.html')


@login_required
def windowsdl(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        ssh('10.0.0.164',58022,'bohan','sudo su - app','echo "%s" > /home/app/nginx/html/windowsdl.html'%AA)
        ss = os.popen('curl windowsdl.weiyoucrm.com').read().strip()
        logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
        return render_to_response('auto/windowsdl.html',{'ss':'通过获取当前网页信息，得到版本号为:%s'%ss})
    else:
        return render_to_response('auto/windowsdl.html')


class TUForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()
def turegist(req):
    if req.method == 'POST':
        uf = TUForm(req.POST,req.FILES)
        if uf.is_valid():
            PATH = uf.cleaned_data['username']
            AA = uf.cleaned_data['headImg'].name
            fp = file('/home/app/upload_demo/upload/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            DIR = '/home/app/upload_demo/upload/%s' %AA
            T = os.popen('/usr/bin/fdfs_upload_file /etc/fdfs/client.conf %s'%DIR).read().strip()
            SIZE = T.replace(".", "_%s."%PATH)
            TU = 'http://img01.taotaosou.cn/size/%s' %SIZE
            #logger.info('PATH: %s file_name: %s' % (PATH, AA))
            return HttpResponse(TU)
        else:
            AA = uf.cleaned_data['headImg'].name
            fp = file('/home/app/upload_demo/upload/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            DIR = '/home/app/upload_demo/upload/%s' %AA
            T = os.popen('/usr/bin/fdfs_upload_file /etc/fdfs/client.conf %s'%DIR).read().strip()
            TU = 'http://img01.taotaosou.cn/%s' %T
            return HttpResponse(TU)
    else:
        uf = UserForm()
    return render_to_response('turegist.html',{'uf':uf})



class VideoForm(forms.Form):
    headImg = forms.FileField()
def videoup(req):
    if req.method == 'POST':
        uf = VideoForm(req.POST, req.FILES)
        if uf.is_valid():
            AA = uf.cleaned_data['headImg'].name
            fp = file('/home/app/upload_demo/videoup/'+uf.cleaned_data['headImg'].name, 'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            up = upyun.UpYun('qlyvideo1','ttsly', 'taotaosou')
            BB = u'/home/app/upload_demo/videoup/%s'%AA
            with open(BB, 'rb') as f:
                res = up.put('/video/%s'%AA, f, checksum=True)
            CC = 'http://qlyvideo1.b0.upaiyun.com/video/%s'%AA
            logger.info('filename:%s  dir: %s'%(AA,BB))
            return HttpResponse(CC)
    else:
        uf = VideoForm()
    return render_to_response('videoup.html',{'uf':uf})


@login_required
def spsellercp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/spseller/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/spseller/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def spsellerdep_52(req):
       sun = ssh('192.168.4.52',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py weishop /home/app/tomcat-8.0.15-weishop_seller-8480/ weishop_seller-8480 /nfsdata/bohan/sypt-super/spseller/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def spsellerhg_52(req):
       sun = ssh('192.168.4.52',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py weishop_seller /home/app/tomcat-8.0.15-weishop_seller-8480/  weishop_seller-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def spsellerlog_52(req):
       sun = ssh('192.168.4.52',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-weishop_seller-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})
	   
def spsellerdep_53(req):
       sun = ssh('192.168.4.53',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py weishop /home/app/tomcat-8.0.15-weishop_seller-8480/ weishop_seller-8480 /nfsdata/bohan/sypt-super/spseller/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def spsellerhg_53(req):
       sun = ssh('192.168.4.53',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py spseller /home/app/tomcat-8.0.15-weishop_seller-8480/  weishop_seller-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def spsellerlog_53(req):
       sun = ssh('192.168.4.53',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-weishop_seller-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})	   


@login_required
def weishop_tpregister(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/weishop_tp/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/weishop_tp/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def shop_tpdep_56(req):
       sun = ssh('192.168.4.56',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py weishop /home/app/tomcat-8.0.15-weishop_tp-8480/ weishop_tp-8480 /nfsdata/bohan/sypt-super/weishop_tp/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def shop_tphg_56(req):
       sun = ssh('192.168.4.56',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py weishop /home/app/tomcat-8.0.15-weishop_tp-8480/  weishop_tp-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def shop_tplog_56(req):
       sun = ssh('192.168.4.56',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-weishop_tp-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def weishop_apicp(req):
    if req.method == 'POST':
        os.system('rm -rf /nfsdata/bohan/sypt-super/weishop_api/*')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/weishop_api/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})





def weishop_apidep_54(req):
       sun = ssh('192.168.4.54',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py weishop /home/app/tomcat-8.0.15-weishop_api-8480/ weishop_api-8480 /nfsdata/bohan/sypt-super/weishop_api/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def weishop_apihg_54(req):
       sun = ssh('192.168.4.54',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py weishop_api /home/app/tomcat-8.0.15-weishop_api-8480/  weishop_api-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def weishop_apilog_54(req):
       sun = ssh('192.168.4.54',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-weishop_api-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})



def weishop_apidep_55(req):
       sun = ssh('192.168.4.55',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/bs_dq.py weishop /home/app/tomcat-8.0.15-weishop_api-8480/ weishop_api-8480 /nfsdata/bohan/sypt-super/weishop_api/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def weishop_apihg_55(req):
       sun = ssh('192.168.4.55',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/hg.py weishop_api /home/app/tomcat-8.0.15-weishop_api-8480/  weishop_api-8480')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'tts','ss':ss})

def weishop_apilog_55(req):
       sun = ssh('192.168.4.55',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/log.py /home/app/tomcat-8.0.15-weishop_api-8480/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/log.html',{'title':'tts','ss':ss})

@login_required
def registerwsbackdep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/wsback/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/wsback/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def qdwsbackdep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  wsback /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/wsback/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdyunkefucs','ss':ss})


@login_required
def registerqlyexondep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/qlyexon/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qlyexon/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def qdqlyexondep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  qlyexon /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/qlyexon/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdyunkefucs','ss':ss})


def youcheqd(req):
    if req.method == 'POST':
        AA = req.POST['a1']
        BB = req.POST['b1']
        CC = req.POST['c1']
       # url = "http://199.155.122.116:8022/syncIndex.do?v1=%s&v2=%s&v3=%s"%(AA,BB,CC)
        url = "http://114.55.57.181:30003/youche/cacheFrontResouce.do?css=%s&appJs=%s&vendorJs=%s"%(AA,CC,BB)
        conn = httplib.HTTPConnection("114.55.57.181:30003")
        conn.request(method="GET", url=url)
        response = conn.getresponse()
        res = response.read()
        logger.info('当用户:-%s-,执行函数名:%s ' % (req.user, sys._getframe().f_code.co_name))
        return render_to_response('youcheqd.html',{'ss': res})
    else:
        return render_to_response('youcheqd.html')

@login_required
def registerqlyyouchedep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/qlyyouche/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/qlyyouche/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def qdqlyyouchedep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  qly-youche /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/qlyyouche/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdyunkefucs','ss':ss})


def tus(req):
    if req.method == 'POST':
        DIR = '/usr/tupfile/'
        os.system('rm -rf %s*'%DIR)
        uf = VideoForm(req.POST,req.FILES)
        if uf.is_valid():
            files = req.FILES.getlist('headImg')
            for f in files:
                destination = open(DIR + f.name,'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            AA = glob.glob(r"%s*"%DIR)
            list = []
            for i in AA:
                T = os.popen('fdfs_upload_file /etc/fdfs/client.conf   %s'%i).read().strip()
                TT = 'http://img.taotaosou.com/%s'%T
                list.append(TT)

            return render_to_response('tus2.html',{'list':list})

    else:
        uf = UserForm()
    return render_to_response('tus1.html',{'uf':uf})


@login_required
def registerqly_title(req):   #chage
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qly_title/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qly_title/'   #chage
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})  #chage




def qly_titledep_123(req):
       sun = ssh('192.168.3.123',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  qly_title /home/app/title-score-server /nfsdata/bohan/sypt-super/qly_title/title-score-server-*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly_title','ss':ss})

def qly_titledep_125(req):
       sun = ssh('192.168.3.125',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py   qly_title /home/app/title-score-server /nfsdata/bohan/sypt-super/qly_title/title-score-server-*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly_title','ss':ss})

def qly_titledep_127(req):
       sun = ssh('192.168.3.127',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/br_bs.py  qly_title /home/app/title-score-server /nfsdata/bohan/sypt-super/qly_title/title-score-server-*.zip')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'qly_title','ss':ss})


@login_required
def registerceshitextdep(req):
    if req.method == 'POST':
        os.system('rm -rf  /nfsdata/bohan/sypt-super/qianduan/ceshitext/*.zip')
        form = UserForm(req.POST)
        if form.is_valid():
            DD = form.cleaned_data
            try:
                PP = DD['name']
                cc = os.path.basename(PP)
                PATH1 = '/nfsdata/bohan/sypt-super/qianduan/ceshitext/'
                t = paramiko.Transport(("10.0.0.36",58022))
                t.connect(username = "patch", password = "ta0ta0s0u")
                sftp = paramiko.SFTPClient.from_transport(t)
                remotepath='/home/patch/%s' %PP
                localpath=  PATH1 + cc
                sftp.get(remotepath, localpath)
                t.close()
                logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
                return HttpResponse('***10.0.0.36:%s***  to ***%s*** cp OK' % (remotepath,localpath))
            except :
                return HttpResponse('path error')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def qdceshitextdep_86(req):
       sun = ssh('10.0.0.86',58022,'bohan','sudo su - app','/nfsdata/bohan/sypt-super/shell/qd.py  ceshitext /home/app/data/tts/  /nfsdata/bohan/sypt-super/qianduan/ceshitext/')
       ss = sun.split('\n')
       logger.info('当用户:-%s-,执行函数名:%s '%(req.user,sys._getframe().f_code.co_name))
       return render_to_response('auto/dep-bijia.html',{'title':'log-qdyunkefucs','ss':ss})



