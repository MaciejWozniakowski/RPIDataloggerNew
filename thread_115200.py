from os import error
from read_data_115200 import run_and_read_client_115200
import database
import time 
import datetime
from os.path import isfile
ctr = 1
#ctr = 86398 

while True:
    try:
        #

        if isfile('data_from_all_meters.db'):
            result115200 = run_and_read_client_115200()
            date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 
            #115200 METERS 
            #
            database.add_DC_data(result115200[0][0], date_now, result115200[0][1:])#data corresponding to meter 89
            database.add_DC_data(result115200[1][0], date_now, result115200[1][1:])#data corresponding to meter 21
            database.add_DC_data(result115200[2][0], date_now, result115200[2][1:])#data corresponding to meter 83
            database.add_DC_data(result115200[4][0], date_now, result115200[4][1:])#data corresponding to meter 26 
            database.add_AC_data(result115200[5][0], date_now, result115200[5][1:])
            time.sleep(1)
            ctr += 1
            if ctr == (2678400):
                print("Entered cleanup_old_entries")
                database.cleanup_old_entries()
                ctr = 1

        else:
            database.create_all_the_tables()
            print("Tables were created")
    except error: 
        pass


    
