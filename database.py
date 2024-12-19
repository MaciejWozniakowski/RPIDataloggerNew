from datetime import datetime
import sqlite3
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
    print(date, entry[0])
    cursor.execute(query, (date, entry[0], entry[1], entry[2], entry[3], entry[4] , entry[5], entry[6],entry[7], entry[8], entry[9], entry[10], entry[11], entry[12]))


    connection.commit()
    cursor.close()
    connection.close()






