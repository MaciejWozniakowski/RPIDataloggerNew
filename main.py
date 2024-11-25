from read_data_115200 import run_and_read_client_115200
import database
import time 
import datetime

from os.path import isfile
def main():
    if isfile('data_from_all_meters.db'):

        result = run_and_read_client_115200()
        print(result)
        database.add_DC_data(result[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[1], result[2], result[3]))#data corresponding to meter 89
        database.add_DC_data(result[4], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[5], result[6], result[7]))#data corresponding to meter 21 
        database.add_DC_data(result[8], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[9], result[10], result[11]))#data corresponding to meter 83
        database.add_DC_data(result[12], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[13], result[14], result[15]))#data corresponding to meter 57 
        database.add_DC_data(result[16], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tuple(result[17], result[18], result[19]))#data corresponding to meter 89
        #database.add_DC_data(result[20], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (result[21], result[22], result[23]))#data corresponding to meter student 1 
        #database.add_DC_data(result[24], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (result[25], result[26], result[27]))#data corresponding to meter student 2 
    else:
        database.create_all_the_tables()


if __name__ == "__main__":
    main()
