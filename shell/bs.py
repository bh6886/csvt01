#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob, os,shutil,zipfile,socket,datetime,time,sys,MySQLdb,smtplib
from email.MIMEText import MIMEText
from email.Header import Header


if len(sys.argv) == 5:
        S1 = sys.argv[1]
        JAVA_F = sys.argv[2]
        JAVA_P = sys.argv[3]
        S4 = sys.argv[4]
        filesRead = r"%s*.war" % S4
else:
        print 'Usage:( ./xxx.py 项目名  完整程序路径  关键目录  提取部署包目录 如：./1.py  show /home/app/tomcat-6.0.35-p4p-mold-8380/ p4p-mold-8380  /opt/)'
        exit(1)
LT = time.strftime('%Y%m%d',time.localtime(time.time()))

JAVA_W = "%swebapps/ROOT/" % JAVA_F
BACK_F = "/home/app/backup/%s-%s/" % (LT,JAVA_P)
CHECK_CONF = 'config.properties'
receiver = ['bohan@taotaosou.com']

list = glob.glob(filesRead)
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

def DirCreate(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

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

def insert(sql):
   conn = MySQLdb.connect(user='root',passwd='taotaosou',host='192.168.3.31',charset='utf8')
   cur = conn.cursor()
   conn.select_db('csvt')
   cur.execute(sql)
   cur.close()
   conn.commit()
   conn.close()


def deply():
        global list
        for i in list:
                basename = os.path.basename(i)
                dirname = os.path.dirname(i)
                BT = basename.split('-')[2]
                lastMod = os.path.getmtime(i)
                mydate = datetime.datetime.fromtimestamp(int(lastMod))
                FT = mydate.strftime('%Y%m%d')
                print LT
                print BT
                print FT
                if LT == BT == FT:
                        if os.path.exists(JAVA_W):
                                pass
                        else:
                                print "No ***%s*** file" % JAVA_W
                                for mail_to in receiver:
                                        send_mail(mail_to,"Ip:::%s.%s.No ***%s*** file" % (sunip,JAVA_P,JAVA_F),"No ***%s*** file" % JAVA_W)
                                exit(1)
                        file_obj = open('/tmp/sun.txt','w')
                        aa = "*** %s *** \n" % basename + "***deploy %s *** \n" % JAVA_P + "---------------------------\nDATE:\n%s\n" % LT +"---------------------------\nHost_IP:::\n%s\n" % sunip
                        file_obj.write(aa)
                        if os.path.exists('/home/app/backup/'):
                                pass
                        else:
                                print 'path 404 ::: /home/app/backup/'
                                for mail_to in receiver:
                                        send_mail(mail_to,"Ip:::%s.%s.path 404 ::: /home/app/backup/" % (sunip,JAVA_P),"path 404 ::: /home/app/backup/")
                                file_obj.close()
                                exit(1)
                        if os.path.exists(JAVA_F):
                                os.chdir('%s/webapps/' % JAVA_F)
                                file_obj.write("!!! Please check the WAR name  ::: ((( %s )))\n" % basename)
                                print "!!!  Please check the WAR name  ::: ((( %s ))) " % basename
                                killme(JAVA_P)
                                file_obj.write("... %s pid is kill success..\n" % JAVA_P)
                                print "... %s pid is kill success.." % JAVA_P
                                if os.path.exists('/home/app/backup/%s-%s' % (LT,JAVA_P)):
                                        file_obj.write("... Backup Skip, have backup after today... \n")
                                        print "... Backup Skip, have backup after today... "
                                else:
                                        shutil.move(JAVA_W,'/home/app/backup/%s-%s' %  (LT,JAVA_P))
                                        file_obj.write("... %s back success ...\n" % JAVA_P)
                                        print "... %s back success ..." % JAVA_P
                                os.system('rm -rf %swork/* && rm -rf %stemp/* && rm -rf %swebapps/ROOT/*' % (JAVA_F,JAVA_F,JAVA_F))
                                file_obj.write("... rmdir work temp %s success ...\n" % JAVA_P)
                                print "... rmdir work temp %s success ... " % JAVA_P
                                ZIP_D = dirname+'/'+basename
                                DirCreate(JAVA_W)
                                os.system('unzip -o %s -d %s > /dev/null 2>&1' % (ZIP_D,JAVA_W))
                                file_obj.write("... unzip OK ...\n")
                                print "... unzip OK ..."
                                if os.path.isfile('%sWEB-INF/classes/%s' % (JAVA_W,CHECK_CONF)):
                                    os.system('\cp -r  %sWEB-INF/classes/*.properties %sWEB-INF/classes/ ' % (BACK_F,JAVA_W))
                                    file_obj.write("... cp OK path:::/WEB-INF/classes/ ...\n")
                                    print "... cp OK path:::/WEB-INF/classes/ ..."
                                elif os.path.isfile('%sWEB-INF/classes/config/%s' % (JAVA_W,CHECK_CONF)):
                                    os.system('\cp -r  %sWEB-INF/classes/config/*.properties %sWEB-INF/classes/config/ ' % (BACK_F,JAVA_W))
                                    file_obj.write("... cp OK path:::/WEB-INF/classes/ ...\n")
                                    print "... cp OK path:::/WEB-INF/classes/ ..."
                                else :
                                    for mail_to in receiver:
                                        send_mail(mail_to,"Ip:::%s.%s.!!!!!!The configuration file copy back failure" % (sunip,JAVA_P),"NO PATH")
                                    print "Ip:::%s.%s.!!!!!!The configuration file copy back failure" % (sunip,JAVA_P)
                                    file_obj.close()
                                    exit(1)

                                os.system("%sbin/startup.sh >/dev/null" % JAVA_F )
                                MPID = mypid(JAVA_P)
                                print "... Start Success. Process is: %s" % MPID
                                file_obj.write("... Start Success. Process is: %s\n" % MPID)

                                if os.path.isfile('%sWEB-INF/classes/%s' % (JAVA_W,CHECK_CONF)):
                                        check = os.popen('grep -E "199.155.122|172.16.3" %sWEB-INF/classes/* |wc -l ' % JAVA_W).read().strip()


                                elif os.path.isfile('%sWEB-INF/classes/config/%s' % (JAVA_W,CHECK_CONF)):
                                        check = os.popen('grep -E "199.155.122|172.16.3" %sWEB-INF/classes/config/* |wc -l ' % JAVA_W).read().strip()

                                else :

                                        for mail_to in receiver:
                                                send_mail(mail_to,"Ip:::%s.%s.!!!!!!Check the configuration file failed" % (sunip,JAVA_P),"NO PATH")
                                        file_obj.close()
                                        exit(1)

                                if check < '3':
                                        print "... Success.The configuration file check is complete: %s" % JAVA_P
                                        file_obj.write("... Success.The configuration file check is complete: %s\n" % JAVA_P)
                                else:
                                        print "... ERROR:::The configuration file is test address, please check!!!: %s" % JAVA_P
                                        for mail_to in receiver:
                                                send_mail(mail_to,"Ip:::%s.%s.!!!!!!... ERROR:::The configuration file is test address, please check!!!" % (sunip,JAVA_P),"The configuration file ERROR.")
                                                print "Ip:::%s.%s.!!!!!!... ERROR:::The configuration file is test address, please check!!!" % (sunip,JAVA_P),"The configuration file ERROR."
                                        file_obj.close()
                                        exit(1)
                                file_obj.close()
                                file_sun1 = open('/tmp/sun.txt','r')
                                s = file_sun1.read()
                                file_sun1.close()
                                sql = '''insert into Deployment_record(time,deploy,war,message) value(now(),'%s','%s','%s')'''  % (S1,basename,s)
                                insert(sql)
                                for mail_to in receiver:
                                        send_mail(mail_to,"Ip:::%s.%s.deploy Complete!!" % (sunip,JAVA_P),s)
                              #  shutil.move('%s/%s' % (dirname,basename),'%s/%s.bak' % (dirname,basename))
                        else:
                                print 'no %s' % JAVA_F
                                for mail_to in receiver:
                                        send_mail(mail_to,"Ip:::%s.%s.no %s" % (sunip,JAVA_P,JAVA_F),'no %s' % JAVA_F)
                                exit(1)



