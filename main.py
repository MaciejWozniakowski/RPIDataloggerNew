from os import error
import sqlite3
from read_data_115200 import run_and_read_client_115200
from read_data_9600 import run_and_read_client_9600
import database
import time 
import datetime

from os.path import isfile
def main():
    while True:
        try:
            #

            if isfile('data_from_all_meters.db'):

                result = run_and_read_client_115200()
                date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                #result_student = run_and_read_client_9600() 
                print("115200", result[0][0],date_now , result[1][1:])
                #print("9600 result", result_student)
                database.add_DC_data(result[0][0], date_now, result[0][1:])#data corresponding to meter 89
                database.add_DC_data(result[1][0],date_now  , result[1][1:])#data corresponding to meter 21
                database.add_DC_data(result[2][0], date_now, result[2][1:])#data corresponding to meter 83
                database.add_DC_data(result[3][0], date_now, result[3][1:])#data corresponding to meter 57 
                database.add_DC_data(result[4][0], date_now, result[4][1:])#data corresponding to meter 26 
                #database.add_DC_data(result_student[0], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (result[1], result[2], result[3]))#data corresponding to meter student 1 
                #database.add_DC_data(result_student[4], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (result[5], result[6], result[7]))#data corresponding to meter student 2 
            
                #only for test purposes
                conn = sqlite3.connect("data_from_all_meters.db")
                cursor = conn.cursor() 
                cursor.execute("SELECT * FROM DCmeter_89 LIMIT 1")
                print("DC 89 ",cursor.fetchone(),"\n")
                cursor.execute("SELECT * FROM DCmeter_21 LIMIT 1")
                print("DC 21",cursor.fetchone(),"\n")
                cursor.execute("SELECT * FROM DCmeter_83 LIMIT 1")
                print("DC 83 ",cursor.fetchone(),"\n")
                cursor.execute("SELECT * FROM DCmeter_57 LIMIT 1")
                print("DC 57 ",cursor.fetchone()),"\n"
                cursor.execute("SELECT * FROM DCmeter_26 LIMIT 1")
                print("DC 26 ",cursor.fetchone(),"\n")
                cursor.close()
                conn.close()


            else:
                database.create_all_the_tables()
            time.sleep(1)
        except error: 
            print("sth wrong")


        

if __name__ == "__main__":
    main()
