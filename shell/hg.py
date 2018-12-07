#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob, os,shutil,zipfile,socket,datetime,time,sys,MySQLdb,smtplib
from email.MIMEText import MIMEText
from email.Header import Header


if len(sys.argv) == 4:
        S1 = sys.argv[1]
        JAVA_F = sys.argv[2]
        JAVA_P = sys.argv[3]
else:
        print 'Usage:( ./xxx.py 项目名 完整程序路径 关键目录 例如：./2.py  show /home/app/tomcat-6.0.35-p4p-mold-8380/ p4p-mold-8380)'
        exit(1)
LT = time.strftime('%Y%m%d',time.localtime(time.time()))

JAVA_W = "%swebapps/ROOT/" % JAVA_F
BACK_F = "/home/app/backup/%s-%s/" % (LT,JAVA_P)
receiver = ['bohan@taotaosou.com']


def insert(sql):
   conn = MySQLdb.connect(user='root',passwd='taotaosou',host='192.168.3.31',charset='utf8')
   cur = conn.cursor()
   conn.select_db('csvt')
   cur.execute(sql)
   cur.close()
   conn.commit()
   conn.close()


def killme(tag):
    context = os.popen('ps -ef | grep %s | grep -v grep |grep -v cronolog| grep -v tail |grep -v ".py"|  awk \'{print $2}\'' % tag).read().strip()
    if len(context) == 0: return
    pid = int(context)
    os.system('kill -9 %s' %pid)

def mypid(tag):
    context = os.popen('ps -ef | grep %s | grep -v grep |grep -v cronolog| grep -v tail |grep -v ".py"| awk \'{print $2}\'' % tag).read().strip()
    if len(context) == 0: return
    pid = int(context)
    return pid

def get_my_ip():
        try:
                csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                csock.connect(('192.168.3.1', 80))
                (addr, port) = csock.getsockname()
                csock.close()
                return addr
        except socket.error:
                return "127.0.0.1"
sunip = get_my_ip()


def send_mail(to_list,sub,content):
        mail_host="mail.taotaosou.com"
        mail_user="bohan@taotaosou.com"
        mail_pass="80231886"
        msg = MIMEText(content)
        msg['Subject'] = sub
        msg['From'] = mail_user
        msg['To'] = to_list
        try:
                s = smtplib.SMTP()
                s.connect(mail_host)
                s.login(mail_user,mail_pass)
                s.sendmail(mail_user, to_list, msg.as_string())
                s.close()
                return True
        except Exception, e:
                print str(e)
                return False

def cpdir(src,dst):
    shutil.copytree(src, dst)

def rollback():
    if os.path.exists(BACK_F):
        file_obj = open('/tmp/sun.txt','w')
        file_obj.write("1.%s File exists.\n" % BACK_F)
        print "1.%s File exists." % BACK_F
        killme(JAVA_P)
        file_obj.write("2.Service process off\n")
        print "2.Service process off"
        os.system('rm -rf %swork/* && rm -rf %stemp/* && rm -rf %swebapps/ROOT' % (JAVA_F,JAVA_F,JAVA_F))
        file_obj.write("3.War packet deletion.\n")
        print "3.War packet deletion."
        cpdir(BACK_F,'%swebapps/ROOT/' % JAVA_F)
        file_obj.write("4.Rollback completion.\n")
        print "4.Rollback completion."
        os.system("%sbin/startup.sh >/dev/null" % JAVA_F )
        MPID = mypid(JAVA_P)
        file_obj.write("5... Start Success. Process is: %s\n" % MPID)
        print "5.... Start Success. Process is: %s" % MPID
        file_obj.close()
        file_sun1 = open('/tmp/sun.txt','r')
        s = file_sun1.read()
        file_sun1.close()
        sql = '''insert into Rollback_record(time,deploy,message) value(now(),'%s','%s')'''  % (S1,s)
        insert(sql)
        for mail_to in receiver:
            send_mail(mail_to,"Ip:::%s.%s.Rollback success!!" % (sunip,JAVA_P),s)

    else:
        print "%s : No backup file today" % BACK_F
        for mail_to in receiver:
            send_mail(mail_to,"Ip:::%s.%s.Rollback failure!!" % (sunip,JAVA_P),"%s : No backup file today" % BACK_F)
rollback()
