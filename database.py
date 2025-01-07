from datetime import datetime
import asyncio
import sqlite3
from dateutil.relativedelta import relativedelta
# Connect to SQLite database

# Create tables if they don't exist
def create_all_the_tables():
    connection = sqlite3.connect("data_from_all_meters.db")
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_89 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_21 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_83 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_57 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_26 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_3_1 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_3_2 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS ACmeter (date TEXT PRIMARY KEY, U1Nrms REAL, U2Nrms REAL, U3Nrms REAL, I1rms REAL, I2rms REAL, I3rms REAL, P1rms REAL, P2rms REAL, P3rms REAL, Fgrid REAL, Ptotal REAL, Qtotal REAL, Stotal REAL);")

# Sample data to insert (date, voltage, current, power)

# Insert data into DCmeter_89 table

def add_DC_data(meter,date, entry): #this function adds entries to the database 
     
    connection = sqlite3.connect("data_from_all_meters.db")
    cursor = connection.cursor() 
    query = f"INSERT INTO {meter} (date, voltage, current, power) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (date, entry[0], entry[1], entry[2]))


    connection.commit()
    cursor.close()
    connection.close()

def add_AC_data(meter,date, entry):      
    connection = sqlite3.connect("data_from_all_meters.db")
    cursor = connection.cursor() 
    query = f"INSERT INTO {meter} (date , U1Nrms , U2Nrms , U3Nrms , I1rms , I2rms , I3rms , P1rms , P2rms , P3rms , Fgrid , Ptotal , Qtotal , Stotal ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (date, entry[0], entry[1], entry[2], entry[3], entry[4] , entry[5], entry[6],entry[7], entry[8], entry[9], entry[10], entry[11], entry[12]))


    connection.commit()
    cursor.close()
    connection.close()

def cleanup_old_entries():
    try:
        connection = sqlite3.connect("data_from_all_meters.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM DCmeter_89 WHERE date <= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM DCmeter_21 WHERE date <= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM DCmeter_83 WHERE date <= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM DCmeter_57 WHERE  date<= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM DCmeter_26 WHERE  date<= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM DCmeter_3_1 WHERE date  <= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM DCmeter_3_2 WHERE date <= datetime('now', '-3 months')")
        cursor.execute("DELETE FROM ACmeter WHERE date <= datetime('now', '-3 months')")  
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error during cleanup: {e}")


current_date = datetime.now()
# Date three months prior
date1 = current_date - relativedelta(months = 1)
date1 = str(date1)[:-7]
date2 = current_date - relativedelta(months=2)
date2 = str(date2)[:-7]
date3 = current_date - relativedelta(months=3)
date3 = str(date3)[:-7]
date4 = current_date - relativedelta(months=4)
date4 = str(date4)[:-7]

print(date1, date2, date3, date4)

testdata = (1.9, 1.0,1.0)
ACtest = (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 , 1.0, 1.0, 1.0, 1.0, 1.0)
add_AC_data("ACmeter", date1, ACtest)
add_DC_data("DCmeter_89", date2, testdata) 
add_DC_data("DCmeter_21", date3, testdata) 
add_DC_data("DCmeter_83", date4, testdata) 
add_DC_data("DCmeter_57", date3, testdata) 
add_DC_data("DCmeter_26", date4, testdata) 
add_DC_data("DCmeter_3_1", date3, testdata)
add_DC_data("DCmeter_3_2", date3, testdata)
cleanup_old_entries()
