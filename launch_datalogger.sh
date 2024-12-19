#!/usr/bin/bash
#systemctl start nginx

source /home/pwee/MaciejWozniakowskiDatalogger/temp/bin/activate
python3 api.py > api.log 2>&1 &
disown
python3 main.py
