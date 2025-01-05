import database
from datetime import datetime
import sqlite3
dt = []
ent = (1.0, 1.0, 1.0)
for i in range(8):
    dt.append(datetime(2024, 1, 1, 12, 30 , i))
    

database.add_DC_data("DCmeter_89", dt[0], ent)
database.add_DC_data("DCmeter_21", dt[2], ent)
database.add_DC_data("DCmeter_83", dt[3], ent)
database.add_DC_data("DCmeter_57", dt[4], ent)
database.add_DC_data("DCmeter_26", dt[5], ent)
database.add_DC_data("ACmeter", dt[7], ent)

conn = sqlite3.connect("data_from_all_meters.db")
cursor = conn.cursor()

        # Retrieve all table names from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
