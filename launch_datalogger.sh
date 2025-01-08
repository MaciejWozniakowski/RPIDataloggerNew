#!/usr/bin/bash
#systemctl start nginx

cd /home/pwee/MaciejWozniakowskiDatalogger/temp || exit 1
source bin/activate

nohup python3 api.py > api.log 2>&1 &
nohup python3 main.py &
