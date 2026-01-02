import sqlite3
import pandas as pd

DB_PATH = "database/chc.db"

print("Reading data from database...")

QUERY = """
SELECT
  month,
  clinic,
  COUNT(*) AS total_appointments,
  SUM(no_show) AS total_noshows,
  ROUND(AVG(waiting_time_mins), 1) AS avg_wait_mins,
  ROUND(100.0 * (1.0 - AVG(no_show)), 1) AS attendance_rate_pct,
  ROUND(AVG(staff_on_shift), 1) AS avg_staff_on_shift
FROM appointments
GROUP BY month, clinic
ORDER BY month, clinic;
"""

with sqlite3.connect(DB_PATH) as conn:
    kpi = pd.read_sql_query(QUERY, conn)

# Admin-friendly metric: appointments per staff member
kpi["appts_per_staff"] = (kpi["total_appointments"] / kpi["avg_staff_on_shift"]).round(2)

# Add a simple RAG status (Red/Amber/Green)
def rag(row):
    if row["attendance_rate_pct"] < 80 or row["avg_wait_mins"] > 45:
        return "RED"
    if row["attendance_rate_pct"] < 88 or row["avg_wait_mins"] > 30:
        return "AMBER"
    return "GREEN"

kpi["status"] = kpi.apply(rag, axis=1)

kpi.to_csv("reports/monthly_clinic_kpis.csv", index=False)

print("DONE ✅ Report saved: reports/monthly_clinic_kpis.csv")
print("Rows:", len(kpi))
print("Tip: Open reports/monthly_clinic_kpis.csv in Excel")
