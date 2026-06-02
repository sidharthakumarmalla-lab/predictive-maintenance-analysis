# 🔧 Predictive Maintenance & Equipment Failure Analysis

## 📌 Overview

Predictive Maintenance & Equipment Failure Analysis is a Machine Learning project designed to predict potential machine failures before they occur.

The system analyzes machine operating parameters such as temperature, rotational speed, torque, and tool wear to determine whether equipment is likely to fail. This helps organizations reduce downtime, improve operational efficiency, and lower maintenance costs.

The project includes a trained Machine Learning model and a Streamlit web application for real-time predictions.

---

## 🎯 Problem Statement

Unexpected equipment failures can lead to:

- Production downtime
- Increased maintenance costs
- Reduced productivity
- Equipment damage
- Operational inefficiencies

This project aims to proactively identify failure risks using machine learning techniques.

---

## 🚀 Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Machine failure prediction
- Random Forest Classification Model
- Interactive Streamlit web application
- Real-time prediction interface
- Model serialization using Pickle

---

## 🏗️ System Architecture

```text
Machine Dataset
       │
       ▼
Data Cleaning & Preprocessing
       │
       ▼
Feature Engineering
       │
       ▼
Model Training
(Random Forest Classifier)
       │
       ▼
Model Serialization
(model.pkl)
       │
       ▼
Streamlit Web Application
       │
       ▼
Real-Time Failure Prediction
```

---

## 📂 Project Structure

```text
PredictiveMaintenance/
│
├── app.py
├── train_model.ipynb
├── model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── predictive_maintenance.csv
```

---

## 📊 Dataset Information

The dataset contains machine operational parameters:

| Feature | Description |
|----------|-------------|
| Type | Machine Type |
| Air Temperature | Air temperature in Kelvin |
| Process Temperature | Process temperature in Kelvin |
| Rotational Speed | Machine RPM |
| Torque | Torque generated |
| Tool Wear | Tool wear duration |
| Target | Failure / No Failure |

---

## ⚙️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Pickle

### Web Application
- Streamlit

### Development Tools
- Jupyter Notebook
- VS Code
- GitHub

---

## 🤖 Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Why Random Forest?

- Handles non-linear relationships
- Robust against overfitting
- High prediction accuracy
- Works well on structured industrial datasets

---

## 📈 Model Performance

### Accuracy

**98.45%**

### Evaluation Metrics

- Accuracy Score
- Classification Report
- Confusion Matrix

---

## 🖥️ Streamlit Application

The Streamlit application allows users to:

- Select machine type
- Enter operating parameters
- Predict equipment failure risk instantly

### Input Parameters

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

### Output

- Equipment Operating Normally
or
- Machine Failure Predicted

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/predictive-maintenance.git
```

### Step 2: Navigate to Project Folder

```bash
cd predictive-maintenance
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Streamlit App

```bash
streamlit run app.py
```

---

## 💡 Business Impact

This solution can help organizations:

- Reduce unexpected breakdowns
- Improve maintenance planning
- Increase equipment reliability
- Minimize production downtime
- Lower operational costs

---

## 🔮 Future Enhancements

- FastAPI Integration
- Cloud Deployment (AWS/Azure)
- Real-time IoT Data Integration
- Predictive Maintenance Dashboard
- Remaining Useful Life (RUL) Prediction
- Alert & Notification System

---

## 🧠 Key Learnings

Through this project, I gained experience in:

- Data preprocessing
- Exploratory Data Analysis
- Machine Learning model development
- Model deployment concepts
- Streamlit application development
- End-to-end ML workflow implementation

---

## 👨‍💻 Author

### Sidhartha Kumar Malla

B.Tech (Electrical Engineering)

M.Tech (Industrial Engineering & Management)

Skills:
- Python
- SQL
- Power BI
- Machine Learning
- Data Analytics
- Streamlit

---

⭐ If you found this project useful, please consider giving it a star.

