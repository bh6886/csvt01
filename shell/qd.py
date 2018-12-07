#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob, os,shutil,socket,datetime,time,sys,MySQLdb
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header

if len(sys.argv) == 4:
        XM = sys.argv[1]
        TMTDIR = sys.argv[2]
        S3 = sys.argv[3]
        filesRead = r"%s*.zip" % S3
else:
        print 'Usage:( ./xxx.py 工程文件夹名 解压目录 文件提取目录 例如:./1.py  taobao /home/app/nginx/html/ /nfsdata/bohan/ )'
        exit(1)

receiver = ['bohan@taotaosou.com']
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
    TMTBAK='/home/app/backup/'
    LT =  time.strftime('%Y%m%d',time.localtime(time.time()))
    list = glob.glob(filesRead)
    for i in list:
        basename = os.path.basename(i)
        dirname = os.path.dirname(i)
        lastMod = os.path.getmtime(i)
        mydate = datetime.datetime.fromtimestamp(int(lastMod))
        FT = mydate.strftime('%Y%m%d')
        if LT == FT:
            file_obj = open('/tmp/sun.txt','w')
            aa = "*** %s *** \n" % basename + "***deploy %s *** \n" % XM + "---------------------------\nDATE:\n%s\n" % LT +"---------------------------\nHost_IP:::\n%s\n" % sunip
            file_obj.write(aa)
            if os.path.exists(TMTDIR+XM):
                if os.path.exists(TMTBAK+XM+LT):
                    os.system('rm -rf %s%s' % (TMTDIR,XM))
                else:
                    shutil.move(TMTDIR+XM,TMTBAK+XM+LT)
            else:
                print '文件不存在'
                exit(1)
            ZIP_D = dirname+'/'+basename
            a = os.popen('unzip -d %s%s  %s' % (TMTDIR,XM,ZIP_D)).read().strip('\n')
            print a
            file_obj.write("%s" % a)
            print "... unzip OK ..."
            file_obj.write("\n... unzip OK ...")
            file_obj.close()

            file_sun1 = open('/tmp/sun.txt','r')
            s = file_sun1.read()
            file_sun1.close()
            b = os.popen('head -12 /tmp/sun.txt').read().strip('\n')

            file_sun1.close()
            for mail_to in receiver:
                send_mail(mail_to,"Ip:::%s.%s deploy Complete!!" % (sunip,XM),s)
            os.system('rm -rf %s' % ZIP_D)
            sql = '''insert into QD_record(time,deploy,message) value(now(),'%s','%s')'''  % (XM,b)
            insert(sql)
        else:
            print "没有找到合适部署zip包"



deply()
