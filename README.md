Project Overview

The Customer Churn Prediction System is a machine learning-powered web application designed to predict whether a customer is likely to discontinue their telecom services (churn). The application leverages a Random Forest Classifier trained on a structured telecom dataset and employs SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalance. This system enables telecom service providers to proactively identify high-risk customers and take targeted actions to retain them.
The project is developed using Python for the backend, scikit-learn for machine learning, and Streamlit for building a lightweight and interactive user interface.

Problem Statement

Customer retention is a critical aspect of business growth in the telecom industry. Acquiring new customers often incurs higher costs than retaining existing ones. However, identifying customers likely to churn is a complex task due to the non-linear relationships between factors like demographics, usage patterns, billing behavior, and customer support interactions.

This project aims to address the problem by:

  1. Applying machine learning techniques to detect patterns in customer behavior.

  2. Creating a user-friendly interface for real-time predictions.

  3. Using SMOTE to address the class imbalance problem, which is common in churn datasets.

Project Goals

  1. Predict the likelihood of customer churn using machine learning classification.

  2. Enable real-time predictions through an interactive web application.

  3. Provide business users with interpretable outputs to support retention strategies.

1. Data Source
   
Dataset: tel_churn.csv

Features: Includes customer demographics (e.g., gender, age), account information (e.g., tenure, contract), service usage (e.g., streaming, tech support), and billing data (e.g., total charges, payment method).

Target Variable: Churn (binary: Yes/No)

2. Model Development (Offline)
The machine learning pipeline was implemented outside the Streamlit app (app.py) and includes the following steps:

a. Data Preprocessing
Handled missing values and outliers.

Applied one-hot encoding to categorical features.

Normalized or standardized numerical features if required.

b. Handling Imbalance
Applied SMOTE to oversample the minority class (churn) and balance the dataset.

c. Model Training
Algorithm used: Random Forest Classifier (from scikit-learn)

Performance metrics evaluated: Accuracy, Precision, Recall, F1-Score, ROC-AUC

d. Model Serialization
The final trained model was saved using the pickle library as model_rf_smote.sav.

3. Web Interface (app.py - Streamlit)
   
a. User Input
Collects real-time customer data using Streamlit widgets such as dropdowns and number inputs.

Inputs include:

  1. Senior Citizen status

  2. Monthly and Total Charges

  3. Gender, Partner, Dependents

  4. Internet service type

  4. Use of online security, tech support, and streaming services

  5. Contract type and payment method

  6 Tenure group (e.g., 1–12 months, 13–24 months, etc.)

b. Feature Encoding
Transforms user input into a one-hot encoded DataFrame.

Aligns input features with the structure expected by the trained model.

c. Model Inference
Loads the trained model using pickle.

Predicts churn status (0 = Stay, 1 = Churn).

Calculates and displays the prediction confidence score.

d. Logging
Logs model load and prediction events using Python’s logging module.

Log file: streamlit_app.log


