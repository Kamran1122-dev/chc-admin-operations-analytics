import numpy as np
import pandas as pd

print("Script started...")

rng = np.random.default_rng(42)

def make_chc_data(n=4000):
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=365).to_series()
    appt_date = rng.choice(dates.values, size=n, replace=True)

    clinics = rng.choice(
        ["CHC-Cardio","CHC-Diabetes","CHC-Respiratory","CHC-Physio","CHC-MentalHealth"],
        size=n
    )

    appt_type = rng.choice(["Follow-up","New","Review","Telehealth"], size=n)
    age_band = rng.choice(["0-17","18-34","35-49","50-64","65+"], size=n)
    deprivation = rng.integers(1, 6, size=n)

    hour = rng.choice([8,9,10,11,12,13,14,15,16], size=n)
    prior_appts = rng.integers(0, 10, size=n)
    prior_noshows = rng.integers(0, 3, size=n)

    no_show = rng.binomial(1, 0.15, size=n)
    waiting_time = rng.integers(5, 90, size=n)
    staff = rng.integers(3, 10, size=n)

    df = pd.DataFrame({
        "appointment_id": range(1, n+1),
        "appointment_date": appt_date,
        "appointment_hour": hour,
        "clinic": clinics,
        "appointment_type": appt_type,
        "age_band": age_band,
        "deprivation_index": deprivation,
        "prior_appointments": prior_appts,
        "prior_noshows": prior_noshows,
        "waiting_time_mins": waiting_time,
        "staff_on_shift": staff,
        "no_show": no_show
    })

    df["weekday"] = pd.to_datetime(df["appointment_date"]).dt.day_name()
    df["month"] = pd.to_datetime(df["appointment_date"]).dt.to_period("M").astype(str)
    return df

if __name__ == "__main__":
    df = make_chc_data()
    df.to_csv("data/chc_appointments.csv", index=False)
    print("DONE ✅ Dataset created")
    print("Rows:", len(df))
