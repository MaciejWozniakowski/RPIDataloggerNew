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
                result_student = run_and_read_client_9600() 
                print("115200", result)
                print("9600 result", result_student)
                database.add_DC_data(result[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[1], result[2], result[3]))#data corresponding to meter 89
                database.add_DC_data(result[4], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[5], result[6], result[7]))#data corresponding to meter 21 
                database.add_DC_data(result[8], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[9], result[10], result[11]))#data corresponding to meter 83
                database.add_DC_data(result[12], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[13], result[14], result[15]))#data corresponding to meter 57 
                database.add_DC_data(result[16], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[17], result[18], result[19]))#data corresponding to meter 26 
                database.add_DC_data(result_student[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (result[1], result[2], result[3]))#data corresponding to meter student 1 
                database.add_DC_data(result_student[4], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (result[5], result[6], result[7]))#data corresponding to meter student 2 
            
                #only for test purposes
                conn = sqlite3.connect("data_from_all_meters.db")
                cursor = conn.cursor() 
                cursor.execute("SELECT * FROM DCmeter_89 LIMIT 1")
                print(cursor.fetchone())
                cursor.execute("SELECT * FROM DCmeter_21 LIMIT 1")
                print(cursor.fetchone())
                cursor.execute("SELECT * FROM DCmeter_83 LIMIT 1")
                print(cursor.fetchone())
                cursor.execute("SELECT * FROM DCmeter_57 LIMIT 1")
                print(cursor.fetchone())
                cursor.execute("SELECT * FROM DCmeter_26 LIMIT 1")
                print(cursor.fetchone())
                cursor.execute("SELECT * FROM DCmeter_3_1 LIMIT 1")
                print(cursor.fetchone())
                cursor.execute("SELECT * FROM DCmeter_3_2 LIMIT 1")
                print(cursor.fetchone())
                cursor.close()
                conn.close()


            else:
                database.create_all_the_tables()
            time.sleep(1)
        except error: 
            print("sth wrong")


        

if __name__ == "__main__":
    main()
