#! /usr/bin/env python
def noautolizi(dir):
 list = os.listdir(dir)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isfile(filepath):
         WAR = filepath
 aa = "tts_client is not autoconfig, complete copy!!!"
 print aa
 BAOM = os.path.basename(WAR)
 for line in list:
     filepath = os.path.join(dir,line)
     if os.path.isdir(filepath):
         shutil.copyfile(WAR,filepath+'/'+BAOM)
         os.popen("chmod -R 777 %s/%s" % (filepath,BAOM)).read().strip('\n')
 os.remove(WAR)
 return aa


def haolingzuiauto(req):
     aa = noautolizi('/nfsdata/bohan/sypt-super/mold/')
     print aa
