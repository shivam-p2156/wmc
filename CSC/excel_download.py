import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect("database.db")

# Read data from appointments table
df = pd.read_sql_query("SELECT * FROM appointments", conn)

# Save to Excel file
df.to_excel("Excel_Data/appointments.xlsx", index=False)

conn.close()

print("Excel file created successfully!")
