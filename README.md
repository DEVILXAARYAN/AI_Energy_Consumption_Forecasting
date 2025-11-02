# ⚡ AI-Powered Energy Consumption Forecasting & Anomaly Detection

### 🎓 Minor Project 1 — Department of Computer Science & Engineering

---

## 📘 Overview
This project focuses on analyzing and forecasting household energy consumption using Artificial Intelligence (AI) and Machine Learning (ML) techniques.  
The system predicts future energy usage patterns and detects anomalies such as sudden spikes or abnormal consumption.  
It forms the foundation for an advanced energy optimization and recommendation system (to be developed in Minor Project 2).

---

## 🎯 Objectives
- To forecast future energy consumption using time-series models.
- To detect unusual energy consumption patterns using anomaly detection algorithms.
- To visualize consumption trends for better understanding and decision-making.

---

## 🧩 Features
✅ Data preprocessing and resampling (hourly, daily)  
✅ Time-series forecasting using **ARIMA** and **XGBoost** models  
✅ Anomaly detection using **Z-Score** and **Isolation Forest**  
✅ Interactive visualizations with **Matplotlib** and **Seaborn**  
✅ Ready to extend for recommendations or web dashboard in Major Project  

---

## 🛠️ Tech Stack
| Category | Technologies Used |
|-----------|------------------|
| **Language** | Python 3.x |
| **Libraries** | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Statsmodels, XGBoost |
| **Environment** | Jupyter Notebook, VS Code |
| **Dataset** | [Household Power Consumption Dataset](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set) |
| **Version Control** | Git & GitHub |

---
## ⚙️ Installation & Setup
### 1. Clone the Repository
Bash

git clone https://github.com/DEVILXAARYAN/AI_Energy_Consumption_Forecasting.git
cd AI_Energy_Consumption_Forecasting

### 2. Create Virtual Environment
Bash

python -m venv venv
venv\Scripts\activate   # On Windows
### or
source venv/bin/activate  # On macOS/Linux

### 3. Install Dependencies
Bash

pip install -r requirements.txt
### 4. Open the Notebook
Bash

jupyter notebook notebooks/Minor_Project1_AI_Energy_Forecasting_Anomaly.ipynb
Run all cells sequentially to generate forecasts and anomaly detection results.

---

## 📊 Project Workflow

### Data Preprocessing:
Cleaning, merging date/time columns, and handling missing data.

### Exploratory Data Analysis (EDA):
Visualizing trends, consumption peaks, and correlations.

### Forecasting:
Building predictive models using ARIMA and XGBoost.

### Anomaly Detection:
Identifying outliers and unusual energy patterns.

### Visualization & Reporting:
Plotting results for better interpretability.

---

## 🧠 Results

Accurate hourly and daily consumption predictions.

Detected anomalies corresponding to unusual usage spikes.

Model performance evaluated using MAE and RMSE metrics.

---

## 🚀 Future Scope (Minor Project 2 & Major)

Implement energy-saving recommendation system.

Deploy as a web dashboard using Streamlit or Flask.

Incorporate real-time data monitoring and alerts.

---

## 👥 Team Members
Name	Role
Aaryan Singh Panwar	    Project Lead / Developer
Divyansh Purey	        Data Preprocessing / Analysis
Khushal Karde           Model Development
Darshan Joshi           Documentation & Testing

---

## 📚 References

UCI Machine Learning Repository — Individual household electric power consumption dataset

Scikit-learn, Statsmodels, and XGBoost official documentation

Research papers on time-series forecasting and anomaly detection

---

## 🧾 License

This project is developed as part of the Minor Project I coursework.
Free to use for academic and learning purposes.