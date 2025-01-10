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
        # STUDENT METERS - 9600 BUS
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_2_1 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_2_2 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_3_1 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_3_2 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_4_1 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_4_2 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
        # AC METER 
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
        cursor.execute("DELETE FROM DCmeter_89 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_21 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_83 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_57 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_26 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_2_1 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_2_2 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_3_1 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_3_2 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_4_1 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM DCmeter_4_2 WHERE date <= DATETIME('now', '-1 year')")
        cursor.execute("DELETE FROM ACmeter WHERE date <= DATETIME('now', '-1 year')")  
        connection.commit()
        connection.close()
    except Exception as e:
        print(f"Error during cleanup: {e}")
#create_all_the_tables()
