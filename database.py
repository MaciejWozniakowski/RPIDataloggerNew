import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("data_from_all_meters.db")

# Create tables if they don't exist
with connection:
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_89 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_21 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_83 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_57 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_26 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_3_1 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS DCmeter_3_2 (date TEXT PRIMARY KEY, voltage REAL, current REAL, power REAL);")
    connection.execute("CREATE TABLE IF NOT EXISTS ACmeter_50 (date TEXT PRIMARY KEY, U1Nrms REAL, U2Nrms REAL, U3Nrms REAL, I1rms REAL, I2rms REAL, I3rms REAL, P1rms REAL, P2rms REAL, P3rms REAL, Fgrid REAL, Ptotal REAL, Qtotal REAL, Stotal REAL);")

# Sample data to insert (date, voltage, current, power)
sample = ["2024-11-24", 1.0, 1.0, 1.0]

# Insert data into DCmeter_89 table
cursor = connection.cursor()
cursor.execute('INSERT INTO DCmeter_89 (date, voltage, current, power) VALUES (?, ?, ?, ?)', sample)

# Commit the transaction to save changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
