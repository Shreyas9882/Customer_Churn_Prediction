📊 Customer Churn Prediction System – AI-Powered Web Application
A Streamlit-based AI web application that predicts customer churn using a trained Random Forest Classifier enhanced with SMOTE to handle class imbalance. The app enables telecom service providers to proactively identify customers likely to leave, empowering them with insights for strategic retention efforts.

❓ Problem Statement
In the telecom industry, retaining existing customers is more cost-effective than acquiring new ones. However, identifying customers at risk of churn can be challenging due to complex and non-linear behavior patterns.

This project addresses the challenge by:

✅ Applying machine learning techniques to detect patterns in customer data.

✅ Building a user-friendly interface for business teams to access predictions.

✅ Ensuring balanced training using SMOTE to combat dataset imbalance.

🧱 Project Architecture
📁 Data Source:
tel_churn.csv: A structured dataset containing customer attributes such as demographics, service usage, billing information, and churn status.

🧠 Model Development (done outside app.py):
Preprocessing: Cleaning and encoding categorical features using one-hot encoding.

Balancing: Applied SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalance (typically more "non-churn" than "churn").

Model Training: Trained using Random Forest Classifier from scikit-learn.

Serialization: Saved the final trained model as model_rf_smote.sav using Python’s pickle library.

🌐 Web Interface (app.py using Streamlit):
Collects real-time user inputs for relevant features like tenure, contract type, online services, etc.

One-hot encodes the input to align with the model’s training schema.

Loads and invokes the model to:

Predict whether the customer will churn or stay.

Provide a confidence score (probability).

Displays results and logs events or errors for debugging and monitoring.

📜 Logging:
Logs successful model loads and errors using Python’s logging module into streamlit_app.log, making the app production-friendly and easy to debug.

Input Parameters
Users provide values for the following categories:

Demographics:

Gender

Senior Citizen status

Partner

Dependents

Billing Information:

Monthly Charges

Total Charges

Service Subscriptions:

Internet Service

Phone Service

Multiple Lines

Online Security

Online Backup

Device Protection

Tech Support

Streaming TV and Movies

Contract & Billing:

Contract Type

Paperless Billing

Payment Method

Tenure Group (1–12 months, 13–24 months, etc.)
