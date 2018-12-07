#!/bin/bash
PATH=/usr/lib64/qt-3.3/bin:/usr/local/jdk/bin:/usr/local/jdk/jre/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/bohan/bin:/bin:/usr/sbin:/home/bohan/bin:/home/bohan/bin:/home/bohan/keychain
killall -9 python
cd /opt/csvt01/bin && python ../manage.py runfcgi method=prefork host=127.0.0.1 port=8080
