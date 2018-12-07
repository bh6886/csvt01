#!/usr/bin/python 
#coding:utf-8 
import glob, os
#from collections import OrderedDict
aa = os.popen("grep -E 'register|cp' all.log |grep -v 'bohan' | awk '{ print  $6 }' > /opt/csvt01/logs/tmp.txt").read().strip()
#os.system("grep -E 'register|cp' all.log |grep -v 'bohan' | awk '{ print  $6 }' > /opt/csvt01/logs/tmp.txt")
#bb = aa.split('-')[1]

res = []


fileName = file('/opt/csvt01/logs/tmp.txt')

while True:
        line = fileName.readline()
        if len(line) ==0:break
        a = line.split('-')[1]
        res.append(a)
        
fileName.close()
#print res

a = {}
for i in res:
  if res.count(i)>1:
    a[i] = res.count(i)
#print (a)



def fun(s):
    d = sorted(s.iteritems(),key=lambda t:t[1],reverse=True)
    return d
     
d = fun(a)

for i in d:
  print i[0]
