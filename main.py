from read_data_115200 import run_and_read_client_115200
import database
import time 
import datetime

from os.path import isfile
def main():
    if isfile('data_from_all_meters.db'):

        result = run_and_read_client_115200()
        print(result)
    else:
        database.create_all_the_tables()


if __name__ == "__main__":
    main()
