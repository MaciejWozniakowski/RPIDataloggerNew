#!/usr/bin/bash
#systemctl start nginx

cd /home/pwee/MaciejWozniakowskiDatalogger/temp || exit 1
source bin/activate

nohup python3 api.py &
nohup python3 thread_9600.py &
nohup python3 thread_115200.py &
