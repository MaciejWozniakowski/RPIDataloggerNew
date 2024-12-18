#!/usr/bin bash
#systemctl start nginx

#source bin/activate
python3 api.py > api.log 2>&1 &
disown
python3 main.py
