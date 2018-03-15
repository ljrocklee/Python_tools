#!/bin/bash
date=`date +%Y%m%d_%-H:%-M:%S`
while :
do
    sleep 30
    pid=`ps -ef|grep "/usr/sbin/orkaudio"|grep -v grep|awk '{print $2}'`
    if [ -z "$pid" ];
    then
        sh /usr/sbin/orkaudio &
        echo "$date can not find orkaudio, I had restart it...." >>log.txt
    fi
done
