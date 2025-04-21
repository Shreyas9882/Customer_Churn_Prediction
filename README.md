Project Overview
The Customer Churn Prediction System is a machine learning-powered web application designed to predict whether a customer is likely to discontinue their telecom services (churn). The application leverages a Random Forest Classifier trained on a structured telecom dataset and employs SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalance. This system enables telecom service providers to proactively identify high-risk customers and take targeted actions to retain them.

The project is developed using Python for the backend, scikit-learn for machine learning, and Streamlit for building a lightweight and interactive user interface.

Problem Statement
Customer retention is a critical aspect of business growth in the telecom industry. Acquiring new customers often incurs higher costs than retaining existing ones. However, identifying customers likely to churn is a complex task due to the non-linear relationships between factors like demographics, usage patterns, billing behavior, and customer support interactions.

This project aims to address the problem by:

Applying machine learning techniques to detect patterns in customer behavior.

Creating a user-friendly interface for real-time predictions.

Using SMOTE to address the class imbalance problem, which is common in churn datasets.

Project Goals
Predict the likelihood of customer churn using ML classification.

Enable real-time predictions through an interactive web application.

Provide business users with interpretable outputs to support retention strategies.

Project Architecture
1. Data Source
Dataset: tel_churn.csv

Features: Includes customer demographics (e.g., gender, age), account information (e.g., tenure, contract), service usage (e.g., streaming, tech support), and billing data (e.g., total charges, payment method).

Target Variable: Churn (binary: Yes/No)

2. Model Development (Offline)
The machine learning pipeline was implemented outside the Streamlit app (app.py) and includes the following steps:

a. Data Preprocessing:

Handled missing values and outliers.

Applied One-Hot Encoding to categorical features.

Normalized or standardized numerical features if required.

b. Handling Imbalance:

SMOTE (Synthetic Minority Over-sampling Technique) was used to oversample the minority class (churn) to ensure balanced class distribution.

c. Model Training:

Algorithm used: Random Forest Classifier (from scikit-learn)

Performance metrics evaluated: Accuracy, Precision, Recall, F1-Score, ROC-AUC

d. Model Serialization:

The final trained model was saved using the pickle library as model_rf_smote.sav.

3. Web Interface (Streamlit - app.py)
a. User Input:

Collects real-time customer data using Streamlit widgets (dropdowns, number inputs, etc.).

Inputs include:

Senior Citizen status

Monthly and Total Charges

Gender, Partner, Dependents

Internet service type

Use of online security, tech support, streaming services

Contract type and payment method

Tenure group (e.g., 1–12 months, 13–24 months, etc.)

b. Feature Encoding:

Transforms user input into a one-hot encoded DataFrame.

Aligns user data with the features expected by the trained model.

c. Model Inference:

Loads the trained model using pickle.

Predicts churn status (binary: 0 = Stay, 1 = Churn).

Calculates and displays the prediction confidence as a probability score.

d. Logging:

Logs success and error messages related to model loading and predictions using Python’s logging module.

Log file: streamlit_app.log

Key Features
Machine Learning-Powered Predictions: Uses a Random Forest model trained on balanced data.

Real-Time Insights: Provides churn predictions and confidence scores based on live user input.

Interactive Web Interface: Simple and intuitive UI for business users without technical expertise.

Feature Alignment: Input data is one-hot encoded to ensure compatibility with the model.

Robust Logging: All events and errors are logged for easier debugging and maintenance.

Input Parameters
The application accepts the following user inputs:

Demographic Information:

Gender

Senior Citizen status (0 or 1)

Partner (Yes/No)

Dependents (Yes/No)

Service Information:

Phone Service

Internet Service (DSL, Fiber optic, No)

Multiple Lines

Online Security

Online Backup

Device Protection

Tech Support

Streaming TV

Streaming Movies

Billing and Account Details:

Monthly Charges

Total Charges

Contract Type (Month-to-month, One year, Two year)

Paperless Billing (Yes/No)

Payment Method

Tenure Group (e.g., 1–12 months, 13–24 months, etc.)

Model Output
Churn Label:

Output: 0 (Customer will stay) or 1 (Customer will churn)

Probability Score:

A float value between 0.0 and 1.0 representing the likelihood of churn

Example: A score of 0.85 implies an 85% probability that the customer will churn

