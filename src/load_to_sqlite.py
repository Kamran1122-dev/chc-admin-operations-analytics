import sqlite3
import pandas as pd

CSV_PATH = "data/chc_appointments.csv"
DB_PATH = "database/chc.db"

print("Loading CSV...")

df = pd.read_csv(CSV_PATH)

print("Connecting database...")

with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("appointments", conn, if_exists="replace", index=False)

print("DONE ✅ Database created:", DB_PATH)
print("Rows loaded:", len(df))
