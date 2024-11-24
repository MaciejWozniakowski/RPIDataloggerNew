import sqlite3
connection = sqlite3.connect("data_from_all_meters.db")
with connection:
    #DC meters 
    #Modbus TCP bus
    connection.execute("CREATE TABLE DCmeter_89 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    connection.execute("CREATE TABLE DCmeter_21 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    connection.execute("CREATE TABLE DCmeter_83 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    connection.execute("CREATE TABLE DCmeter_57 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    connection.execute("CREATE TABLE DCmeter_26 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    #Modbus RTU bus
    connection.execute("CREATE TABLE DCmeter_3_1 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    connection.execute("CREATE TABLE DCmeter_3_2 (date TEXT PRIMARY KEY, voltage[V] REAL, current[I] REAL, power[W] REAL);")
    #AC meter 
    connection.execute("CREATE TABLE ACmeter_50(date TEXT PRIMARY KEY, U1Nrms REAL , U2Nrms REAL, U3Nrms REAL, I1rms REAL, I2rms REAL, I3rms REAL, P1rms REAL, P2rms REAL, P3rms REAL, Fgrid REAL, Ptotal REAL, Qtotal REAL, Stotal REAL);")

    
