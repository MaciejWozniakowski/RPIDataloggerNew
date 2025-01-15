#!/usr/bin/bash
#systemctl start nginx

cd /home/pwee/MaciejWozniakowskiDatalogger/temp || exit 1
source bin/activate

python3 api.py > api.log 2>&1 &
python3 thread_9600.py > thread_9600.log 2>&1 &
python3 thread_115200.py > thread_115200.log 2>&1 &
wait 
