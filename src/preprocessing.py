# src/preprocessing.py
import pandas as pd
import numpy as np
import os

def load_and_parse(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    try:
        df = pd.read_csv(path, sep=';', parse_dates={'datetime': ['Date', 'Time']},
                         infer_datetime_format=True, low_memory=False, na_values=['?'])
    except:
        df = pd.read_csv(path, low_memory=False, na_values=['?'])
        if 'Date' in df.columns and 'Time' in df.columns:
            df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')
        elif 'datetime' in df.columns:
            df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
        df.set_index('datetime', inplace=True)
    if 'datetime' in df.columns:
        df.set_index('datetime', inplace=True)
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

def basic_clean(df):
    df = df.ffill().bfill()
    return df

def resample_hourly(df):
    df = basic_clean(df)
    return df.resample('H').mean()

if __name__ == "__main__":
    p = "../data/household_power_consumption.csv"
    df = load_and_parse(p)
    dfh = resample_hourly(df)
    print("Loaded:", df.shape, "Hourly:", dfh.shape)
    print(dfh.head())
