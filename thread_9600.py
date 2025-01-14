from os import error
from RS485_sync_read_data_9600 import run_and_read_client_9600
import database
import time 
import datetime
from os.path import isfile

while True:
    try:
        #

        if isfile('data_from_all_meters.db'):
            result9600 = run_and_read_client_9600()
            date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 
            #9600 METERS 
            #
            database.add_DC_data(result9600[0][0], date_now, result9600[0][1:])# meter 2_1
            database.add_DC_data(result9600[1][0], date_now, result9600[1][1:])# meter 2_2
            database.add_DC_data(result9600[2][0], date_now, result9600[2][1:])# meter 2_2
            database.add_DC_data(result9600[3][0], date_now, result9600[3][1:])# meter 3_2
            database.add_DC_data(result9600[4][0], date_now, result9600[4][1:])# meter 3_2
            database.add_DC_data(result9600[5][0], date_now, result9600[5][1:])# meter 4_2
            

        else:
            database.create_all_the_tables()
            print("Tables were created")
    except error: 
        pass


