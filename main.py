from os import error
import sqlite3
from read_data_115200 import run_and_read_client_115200
from read_data_9600 import run_and_read_client_9600
import database
import time 
import datetime
from os.path import isfile
start_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    while True:
        try:
            #

            if isfile('data_from_all_meters.db'):

                result115200 = run_and_read_client_115200()
                result9600 = run_and_read_client_9600()
                date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                #result_student = run_and_read_client_9600() 
                #print("9600 result", result_student)
                database.add_DC_data(result115200[0][0], date_now, result115200[0][1:])#data corresponding to meter 89
                database.add_DC_data(result115200[1][0], date_now, result115200[1][1:])#data corresponding to meter 21
                database.add_DC_data(result115200[2][0], date_now, result115200[2][1:])#data corresponding to meter 83
                database.add_DC_data(result115200[3][0], date_now, result115200[3][1:])#data corresponding to meter 57 
                database.add_DC_data(result115200[4][0], date_now, result115200[4][1:])#data corresponding to meter 26 
#                database.add_AC_data(result[5][0], date_now, result[5][1:])
                # data from the 9600 bus
                database.add_DC_data(result9600[0][0], date_now, result9600[0][1:])#data corresponding to meter 26 
                database.add_DC_data(result9600[1][0], date_now, result9600[1][1:])#data corresponding to meter 26 
                time.sleep(1)
                

            else:
                database.create_all_the_tables()
        except error: 
            print("sth wrong")


        

if __name__ == "__main__":
    main()
