
# Customer Churn Prediction System  

---

## Project Overview

- Customer Churn Prediction System is a machine learning-based web application to predict if a customer will discontinue telecom services.
- It uses a Random Forest Classifier trained on a telecom dataset.
- SMOTE is used to address class imbalance by oversampling the minority class.
- The app helps telecom companies identify high-risk customers and take proactive retention actions.
- Developed using Python, scikit-learn, and Streamlit for the web interface.

---

## Problem Statement

- Customer retention is more cost-effective than acquiring new customers.
- Predicting churn is complex due to diverse customer behavior patterns.
- Machine learning is used to detect churn patterns from data.
- A user-friendly interface enables real-time prediction access.
- SMOTE balances the dataset to improve prediction fairness.

---

## Project Goals

- Predict customer churn likelihood using a trained ML model.
- Provide real-time prediction through a web interface.
- Present interpretable results to help business users.

---

## Project Architecture

- Dataset used is `tel_churn.csv`.
- Data includes demographics, account details, services, and billing information.
- Target variable is `Churn`, represented as Yes or No.

- Data preprocessing includes handling missing values and encoding features.
- SMOTE is applied to balance churn vs non-churn classes.
- Random Forest Classifier is trained using scikit-learn.
- Model is saved as `model_rf_smote.sav` using pickle.

- Web interface is built with Streamlit (`app.py`).
- Interface accepts user inputs through widgets like dropdowns and number inputs.
- Inputs include demographics, billing, services used, contract type, and payment method.
- Inputs are one-hot encoded to match training format.
- Model is loaded and used to predict churn (0 or 1).
- Probability score is displayed along with prediction.
- Logging is implemented using Python’s logging module.
- Logs are saved in `streamlit_app.log`.

---

## Key Features

- Predicts churn using a trained Random Forest model.
- Provides real-time prediction based on user inputs.
- Uses Streamlit for interactive and user-friendly interface.
- Ensures data is formatted correctly for the model using one-hot encoding.
- Logs all model activity and errors for debugging.

---

## Input Parameters

- Gender
- Senior Citizen status
- Partner
- Dependents
- Phone Service
- Internet Service
- Multiple Lines
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Monthly Charges
- Total Charges
- Contract Type
- Paperless Billing
- Payment Method
- Tenure Group

---

## Model Output

- Churn prediction as 0 (Stay) or 1 (Churn)
- Probability score between 0.0 and 1.0 indicating confidence
- Example: A score of 0.85 means 85% chance of churn

---

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a10d81d0-e66a-40b0-ad40-e2f2abc88395" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/1b2c9d91-2ab4-473d-bb92-a8777bda0efd" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a5a53154-5280-491f-9a05-f11c4af3b7fc" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/396608fe-6983-4c3a-ae7e-1d4e314f57a7" />
