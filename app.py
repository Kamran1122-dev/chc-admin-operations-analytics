import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="CHC Admin Dashboard", layout="wide")

DB_PATH = "database/chc.db"
REPORT_PATH = "reports/monthly_clinic_kpis.csv"

st.title("🏥 CHC Admin Operations Dashboard (NHS-style)")

@st.cache_data
def load_kpis():
    return pd.read_csv(REPORT_PATH)

@st.cache_data
def load_appointments():
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query("SELECT * FROM appointments", conn)

kpi = load_kpis()
df = load_appointments()

st.sidebar.header("Filters")
clinic = st.sidebar.selectbox("Clinic", ["All"] + sorted(df["clinic"].unique()))
month = st.sidebar.selectbox("Month", ["All"] + sorted(df["month"].unique()))

filtered = df.copy()
if clinic != "All":
    filtered = filtered[filtered["clinic"] == clinic]
if month != "All":
    filtered = filtered[filtered["month"] == month]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Appointments", len(filtered))
c2.metric("Attendance Rate (%)", round(100 * (1 - filtered["no_show"].mean()), 1))
c3.metric("No-show Rate (%)", round(100 * filtered["no_show"].mean(), 1))
c4.metric("Avg Waiting Time (mins)", round(filtered["waiting_time_mins"].mean(), 1))

st.divider()
st.subheader("Monthly Clinic KPIs")
st.dataframe(kpi, use_container_width=True)

st.subheader("Waiting Time Trend")
trend = filtered.groupby("month")["waiting_time_mins"].mean()
st.line_chart(trend)

st.subheader("Download Reports")
with open(REPORT_PATH, "rb") as f:
    st.download_button("Download KPI Report", f, file_name="monthly_clinic_kpis.csv")
