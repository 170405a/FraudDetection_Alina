#  Real-Time Fraud Detection System with Explainable AI

##  Project Overview

This project is an AI-powered fraud detection system built using Machine Learning, Explainable AI (SHAP), and Streamlit Dashboarding.

The system analyzes financial transaction patterns and predicts fraudulent transactions in real time. It also provides explainable insights that help analysts understand why a transaction was flagged as fraud.

#  Problem Statement

Financial fraud causes massive losses globally every year. Traditional rule-based systems fail to detect modern fraud patterns effectively.

This project aims to:
- detect fraud transactions accurately
- handle severe class imbalance
- provide explainable predictions
- visualize fraud insights using an interactive dashboard

#  Technologies Used

| Tool | Purpose |

| Python | Core Programming |
| Pandas / NumPy | Data Processing |
| LightGBM | Fraud Detection Model |
| Scikit-learn | Machine Learning Utilities |
| SMOTE | Imbalance Handling |
| SHAP | Explainable AI |
| Plotly | Interactive Charts |
| Streamlit | Dashboard Deployment |

#  Dataset

Dataset Used:
IEEE-CIS Fraud Detection Dataset

Source:
https://www.kaggle.com/c/ieee-fraud-detection/data

Files Used:
- train_transaction.csv
- train_identity.csv

#  Features Implemented

##  Data Preprocessing
- Missing value handling
- Feature engineering
- Label encoding
- Robust scaling

##  Machine Learning
- LightGBM
- XGBoost
- Isolation Forest

##  Imbalance Handling
- SMOTE Oversampling

##  Explainable AI
- SHAP Summary Plot
- Feature Importance Analysis

##  Dashboard Features
- Real-time prediction
- CSV upload analysis
- Fraud probability scoring
- Risk segmentation
- Interactive charts
- 
# Model Performance

| Model | Accuracy | F1 Score |

| LightGBM | 96.9% | 0.52 |
| XGBoost | 97.5% | 0.59 |
| Isolation Forest | 94.1% | 0.17 |

XGBoost achieved the best balance between precision and recall.

#  Explainable AI

SHAP (SHapley Additive Explanations) was used to explain model predictions.

The dashboard visualizes:
- global feature importance
- fraud-driving features
- model transparency insights

#  Streamlit Dashboard

### Features
- Multi-page dashboard
- Fraud analytics overview
- CSV upload prediction
- SHAP visualization
- Risk analysis

### Live App
https://frauddetectionalina-cg5evmalup2jeg8kr7xmbe.streamlit.app/
#  Project Structure

```text
FraudDetection_Alina/
│
├── analysis.ipynb
├── README.md
├── requirements.txt
│
├── data/
│
├── dashboard/
│   ├── app.py
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── shap_summary.png
│   │
│   ├── pages/
│   │   ├── 1_Overview.py
│   │   ├── 2_Transaction_Explorer.py
│   │   ├── 3_SHAP_Insights.py
