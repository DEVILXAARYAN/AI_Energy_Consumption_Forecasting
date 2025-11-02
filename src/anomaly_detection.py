# src/anomaly_detection.py
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy import stats

def zscore_anomalies(series, threshold=3.0):
    s = series.fillna(method='ffill')
    z = np.abs(stats.zscore(s))
    return series[z > threshold]

def isolation_forest_anomalies(series, contamination=0.01):
    df = pd.DataFrame({'value': series.values}, index=series.index)
    df['hour'] = df.index.hour
    iso = IsolationForest(contamination=contamination, random_state=42)
    iso.fit(df)
    preds = iso.predict(df)
    return df[preds == -1]
