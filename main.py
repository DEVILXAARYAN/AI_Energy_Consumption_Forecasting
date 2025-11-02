from src.preprocessing import load_and_parse, resample_hourly
from src.anomaly_detection import zscore_anomalies, isolation_forest_anomalies
import matplotlib.pyplot as plt

DATA_PATH = r"data\household_power_consumption.csv"

def main():
    df = load_and_parse(DATA_PATH)
    dfh = resample_hourly(df)
    series = dfh['Global_active_power'] if 'Global_active_power' in dfh.columns else dfh.iloc[:,0]
    print("Series length:", len(series))
    # quick plot
    series.plot(figsize=(12,4), title='Global Active Power (hourly)')
    plt.show()
    print("Z-score anomalies:", len(zscore_anomalies(series)))
    print("IsolationForest anomalies:", len(isolation_forest_anomalies(series)))

if __name__ == "__main__":
    main()
