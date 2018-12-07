#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob, os,datetime,time,sys

if len(sys.argv) == 2:
        JAVA_F = sys.argv[1]
else:
        print 'Usage:( ./xxx.py  完整程序路径)'
        exit(1)


def tomcat_log():
    now_time = datetime.datetime.now()
    t =  now_time.strftime('%Y-%m-%d')
#   sun = "tail -n 200  %slogs/catalina.%s.out" % (JAVA_F,t)
    os.system("tail -n 200  %slogs/catalina.%s.out" % (JAVA_F,t))
#   ss = sun.split('\n')
#   print ss

tomcat_log()




