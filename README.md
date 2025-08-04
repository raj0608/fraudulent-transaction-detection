# 🛡 Fraudulent Transaction Detection System

A **Machine Learning-based** solution to detect fraudulent credit card transactions in real-time using **FastAPI** for deployment.

---

## 📌 Features
- **Data Cleaning & Preprocessing**
- **Exploratory Data Analysis (EDA)**: Distribution plots, correlation heatmaps, boxplots
- **Feature Engineering**: Scaling, time features, high-amount flag
- **Class Imbalance Handling** using SMOTE
- **Model Building**: Logistic Regression, Random Forest, XGBoost
- **Hyperparameter Tuning** with Random Search
- **Model Evaluation**: ROC-AUC, Precision, Recall, F1-score
- **Real-Time Prediction API** using FastAPI

---

## 📂 Project Structure
```
Fraudulent Transaction Detection System/
│
├── data/
│   └── creditcard.csv         # Original dataset (Not uploaded due to size)
│
├── notebooks/
│   └── Fraudulent Transaction Detection System.ipynb  # Jupyter Notebook with EDA & model building
│
├── main.py                    # FastAPI app for real-time prediction
├── model.pkl                  # Trained ML model
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore cache, datasets, and virtual env files
└── README.md                  # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/fraudulent-transaction-detection.git
cd fraudulent-transaction-detection
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the FastAPI App
```bash
uvicorn main:app --reload
```

Open in browser:
```
http://127.0.0.1:8000/docs
```

---

## 📊 API Usage

**Example JSON Request:**
```json
{
  "features": [
    -0.50,
    -2.30,
    -2.00,
    -1.80,
    -1.50,
    -0.90,
    0.60,
    1.50,
    -0.75,
    -1.10,
    -2.10,
    -1.60,
    0.85,
    -0.80,
    0.25,
    0.30,
    0.40,
    -2.40
  ]
}

```

**Example JSON Response:**
```json
{
  "fraud_probability": 0.82,
  "is_fraud": 1
}
```

---

## 📈 Model Performance

### Random Forest (Tuned)
- **ROC-AUC:** 0.966
- **Precision (Fraud):** 0.85
- **Recall (Fraud):** 0.78
- **F1-score (Fraud):** 0.81

---

## 📄 Dataset
The dataset used in this project is the **Credit Card Fraud Detection dataset** from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud).

> **Note:** The dataset is not included in the repo because it exceeds GitHub’s file size limit.

---

## 👨‍💻 Author
**Rohan Raj**
- 📧 Email: rohanraj6.rr.rr@gmail.com
- 🔗 GitHub: https://github.com/raj0608

---
