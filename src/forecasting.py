# src/forecasting.py
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mape = np.mean(np.abs((y_true - y_pred) / np.where(y_true==0, 1e-8, y_true))) * 100
    return {"MAE": mae, "RMSE": rmse, "MAPE": mape}

def create_lag_features(series, lags=[1,24,168]):
    df = pd.DataFrame({'y': series})
    for lag in lags:
        df[f'lag_{lag}'] = df['y'].shift(lag)
    df['rolling_mean_24'] = df['y'].shift(1).rolling(window=24).mean()
    return df.dropna()
