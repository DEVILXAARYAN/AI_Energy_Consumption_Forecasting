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

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DEVILXAARYAN/AI_Energy_Consumption_Forecasting.git
cd AI_Energy_Consumption_Forecasting

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Open the Notebook
jupyter notebook notebooks/Minor_Project1_AI_Energy_Forecasting_Anomaly.ipynb