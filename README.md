# CHC Admin Operations Analytics (NHS-style)

A Community Health Centre (CHC) administrative analytics project demonstrating an end-to-end workflow:
synthetic appointment data → SQL database → monthly KPI reporting → interactive Streamlit dashboard.

This project is designed to reflect typical NHS community healthcare administrative challenges (e.g., monitoring attendance/no-shows, waiting time trends, and clinic workload) while respecting data privacy by using synthetic data.

## What this project does (Admin value)
- Generates privacy-safe synthetic CHC appointment data
- Loads data into a SQLite database (simulating admin data systems)
- Produces a monthly clinic KPI report (CSV) for admin reporting
- Provides a Streamlit dashboard for quick operational insights

## Key KPIs
- Total appointments per clinic/month
- No-shows & attendance rate
- Average waiting time
- Appointments per staff (proxy workload)
- RAG status (RED/AMBER/GREEN) based on thresholds

## Tech stack
- Python, Pandas, NumPy
- SQLite (database)
- Streamlit (dashboard)

