from os import error
#from read_data_115200 import run_and_read_client_115200
#from async_read_data_9600 import run_and_read_client_9600
from RS485_sync_read_data_9600 import run_and_read_client_9600
import database
import time 
import datetime
from os.path import isfile

def main():
    ctr = 1
    #ctr = 86398 
    
    while True:
        try:
            #

            if isfile('data_from_all_meters.db'):
                result115200 = run_and_read_client_115200()
                result9600 = run_and_read_client_9600()
                #result9600 = asyncio.run(run_and_read_client_9600())
                date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # 
                #115200 METERS 
                #
                database.add_DC_data(result115200[0][0], date_now, result115200[0][1:])#data corresponding to meter 89
                database.add_DC_data(result115200[1][0], date_now, result115200[1][1:])#data corresponding to meter 21
                database.add_DC_data(result115200[2][0], date_now, result115200[2][1:])#data corresponding to meter 83
                database.add_DC_data(result115200[4][0], date_now, result115200[4][1:])#data corresponding to meter 26 
                database.add_AC_data(result115200[5][0], date_now, result115200[5][1:])
                # 
                #9600 METERS 
                #
                database.add_DC_data(result9600[0][0], date_now, result9600[0][1:])# meter 2_1
                database.add_DC_data(result9600[1][0], date_now, result9600[1][1:])# meter 2_2
                database.add_DC_data(result9600[3][0], date_now, result9600[3][1:])# meter 3_2
                database.add_DC_data(result9600[5][0], date_now, result9600[5][1:])# meter 4_2
                time.sleep(1)
                ctr += 1
                print(ctr)
                if ctr == (365*86400):
                    print("Entered cleanup_old_entries")
                    database.cleanup_old_entries()
                    ctr = 1
                

            else:
                database.create_all_the_tables()
                print("Tables were created")
        except error: 
            pass


        

if __name__ == "__main__":
    main()
