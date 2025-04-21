# Customer_Churn_Prediction
A Streamlit-based AI web application that predicts customer churn using a trained Random Forest Classifier enhanced with SMOTE to handle class imbalance. The app enables telecom service providers to proactively identify customers likely to leave, empowering them with insights for strategic retention efforts.

Problem Statement
In the telecom industry, retaining existing customers is more cost-effective than acquiring new ones. However, identifying customers at risk of churn can be challenging due to complex and non-linear behavior patterns. This project addresses this challenge by:

Applying machine learning techniques to detect patterns in customer data.

Building a user-friendly interface for business teams to access predictions.

Ensuring balanced training using SMOTE to combat dataset imbalance.

Project Architecture
Data Source:

tel_churn.csv: A structured dataset containing customer attributes such as demographics, service usage, billing information, and churn status.

Model Development (done outside the app.py file):

Preprocessing: Cleaning, encoding categorical features using one-hot encoding.

Balancing: Applied SMOTE (Synthetic Minority Over-sampling Technique) to handle class imbalance (more non-churn than churn).

Model Training: Trained using Random Forest Classifier from scikit-learn.

Serialization: The final trained model is saved as model_rf_smote.sav using Python’s pickle library.

Web Interface (Streamlit - app.py):

Collects real-time user input for all relevant features (e.g., tenure, contract type, online services).

One-hot encodes the input to match the model’s training schema.

Loads and invokes the model to predict:

Whether the customer will churn or stay.

The probability (confidence score) of churn.

Displays the result and logs any issues for debugging.

Logging:

Logs successful model loading and errors using Python’s logging module into a file (streamlit_app.log), making it robust and production-ready.

Key Features
 ML-Powered Predictions: Uses a Random Forest model trained on balanced data for high-accuracy predictions.

Real-Time Insights: Provides probability-based churn predictions with a single click.

Interactive UI: Designed with Streamlit for easy use by non-technical stakeholders.

Feature Alignment: One-hot encoded input ensures compatibility with the trained model.

Robust Logging: Tracks and reports issues during model loading and prediction for better maintenance.

Input Parameters
Users can input the following:

Demographics: Gender, Senior Citizen status, Partner, Dependents.

Billing Info: Monthly Charges, Total Charges.

Service Subscriptions: Internet, Phone, Streaming, Online Security, etc.

Contract Type and Tenure Group.

Payment Method and Paperless Billing preference.

Model Output
Churn Label: Binary classification — 0 for staying, 1 for churning.

Probability Score: A float (0.0–1.0) representing the likelihood of churn, giving transparency into model confidence.

