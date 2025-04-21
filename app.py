import streamlit as st
import pandas as pd
import pickle
import logging

# Configure logging
logging.basicConfig(filename='streamlit_app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the model
try:
    with open("model_rf_smote.sav", "rb") as file:
        model = pickle.load(file)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Model loading failed: {e}")
    st.error(f"Model loading failed: {e}")
    model = None

# Check model validity
if not hasattr(model, "predict"):
    st.error("Loaded object is not a valid model.")
    st.stop()

# UI
st.title("Customer Churn Prediction App")

# Load the tel_churn.csv file directly from the folder
file_path = 'tel_churn.csv'
try:
    data = pd.read_csv(file_path)
except Exception as e:
    logging.error(f"Error loading file: {e}")
    st.error(f"Error loading file: {e}")

# Prediction Function
def predict_churn(input_df):
    try:
        # Ensure the input features match the model's expected features
        feature_columns = [
            'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender_Female', 'gender_Male', 
            'Partner_No', 'Partner_Yes', 'Dependents_No', 'Dependents_Yes', 'PhoneService_No', 
            'PhoneService_Yes', 'MultipleLines_No', 'MultipleLines_No phone service', 
            'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic', 
            'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_No internet service', 
            'OnlineSecurity_Yes', 'OnlineBackup_No', 'OnlineBackup_No internet service', 
            'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_No internet service', 
            'DeviceProtection_Yes', 'TechSupport_No', 'TechSupport_No internet service', 
            'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_No internet service', 'StreamingTV_Yes', 
            'StreamingMovies_No', 'StreamingMovies_No internet service', 'StreamingMovies_Yes', 
            'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year', 'PaperlessBilling_No', 
            'PaperlessBilling_Yes', 'PaymentMethod_Bank transfer (automatic)', 
            'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 
            'PaymentMethod_Mailed check', 'tenure_group_1 - 12', 'tenure_group_13 - 24', 
            'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72'
        ]
        
        # Ensure the input data has the same features
        df_encoded = pd.get_dummies(input_df)  # One-hot encode the input data
        df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0)  # Align features with the model

        # Make prediction
        prediction = model.predict(df_encoded)[0]
        probability = model.predict_proba(df_encoded)[:, 1][0]
        return prediction, probability
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        st.error(f"Prediction error: {e}")
        return None, None

# User Inputs (same as before)
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)
gender = st.selectbox("Gender", ["Male", "Female"])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
tenure_group = st.selectbox("Tenure Group", ["1 - 12", "13 - 24", "25 - 36", "37 - 48", "49 - 60", "61 - 72"])

# Prepare input data based on user input
data_input = pd.DataFrame([{
    'SeniorCitizen': SeniorCitizen,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges,
    'gender_Female': 1 if gender == "Female" else 0,
    'gender_Male': 1 if gender == "Male" else 0,
    'Partner_Yes': 1 if Partner == "Yes" else 0,
    'Partner_No': 1 if Partner == "No" else 0,
    'Dependents_Yes': 1 if Dependents == "Yes" else 0,
    'Dependents_No': 1 if Dependents == "No" else 0,
    'PhoneService_Yes': 1 if PhoneService == "Yes" else 0,
    'PhoneService_No': 1 if PhoneService == "No" else 0,
    'MultipleLines_Yes': 1 if MultipleLines == "Yes" else 0,
    'MultipleLines_No': 1 if MultipleLines == "No" else 0,
    'MultipleLines_No phone service': 1 if MultipleLines == "No phone service" else 0,
    'InternetService_DSL': 1 if InternetService == "DSL" else 0,
    'InternetService_Fiber optic': 1 if InternetService == "Fiber optic" else 0,
    'InternetService_No': 1 if InternetService == "No" else 0,
    'OnlineSecurity_Yes': 1 if OnlineSecurity == "Yes" else 0,
    'OnlineSecurity_No internet service': 1 if OnlineSecurity == "No internet service" else 0,
    'OnlineSecurity_No': 1 if OnlineSecurity == "No" else 0,
    'OnlineBackup_Yes': 1 if OnlineBackup == "Yes" else 0,
    'OnlineBackup_No internet service': 1 if OnlineBackup == "No internet service" else 0,
    'OnlineBackup_No': 1 if OnlineBackup == "No" else 0,
    'DeviceProtection_Yes': 1 if DeviceProtection == "Yes" else 0,
    'DeviceProtection_No internet service': 1 if DeviceProtection == "No internet service" else 0,
    'DeviceProtection_No': 1 if DeviceProtection == "No" else 0,
    'TechSupport_Yes': 1 if TechSupport == "Yes" else 0,
    'TechSupport_No internet service': 1 if TechSupport == "No internet service" else 0,
    'TechSupport_No': 1 if TechSupport == "No" else 0,
    'StreamingTV_Yes': 1 if StreamingTV == "Yes" else 0,
    'StreamingTV_No internet service': 1 if StreamingTV == "No internet service" else 0,
    'StreamingTV_No': 1 if StreamingTV == "No" else 0,
    'StreamingMovies_Yes': 1 if StreamingMovies == "Yes" else 0,
    'StreamingMovies_No internet service': 1 if StreamingMovies == "No internet service" else 0,
    'StreamingMovies_No': 1 if StreamingMovies == "No" else 0,
    'Contract_Month-to-month': 1 if Contract == "Month-to-month" else 0,
    'Contract_One year': 1 if Contract == "One year" else 0,
    'Contract_Two year': 1 if Contract == "Two year" else 0,
    'PaperlessBilling_Yes': 1 if PaperlessBilling == "Yes" else 0,
    'PaperlessBilling_No': 1 if PaperlessBilling == "No" else 0,
    'PaymentMethod_Electronic check': 1 if PaymentMethod == "Electronic check" else 0,
    'PaymentMethod_Mailed check': 1 if PaymentMethod == "Mailed check" else 0,
    'PaymentMethod_Bank transfer (automatic)': 1 if PaymentMethod == "Bank transfer (automatic)" else 0,
    'PaymentMethod_Credit card (automatic)': 1 if PaymentMethod == "Credit card (automatic)" else 0,
    'tenure_group_1 - 12': 1 if tenure_group == "1 - 12" else 0,
    'tenure_group_13 - 24': 1 if tenure_group == "13 - 24" else 0,
    'tenure_group_25 - 36': 1 if tenure_group == "25 - 36" else 0,
    'tenure_group_37 - 48': 1 if tenure_group == "37 - 48" else 0,
    'tenure_group_49 - 60': 1 if tenure_group == "49 - 60" else 0,
    'tenure_group_61 - 72': 1 if tenure_group == "61 - 72" else 0,
}])

# Predict when the button is clicked
if st.button("Predict Churn"):
    prediction, probability = predict_churn(data_input)
    
    if prediction is not None:
        if prediction == 0:
            st.success(f"The customer is predicted to stay with the company.")
        else:
            st.warning(f"The customer is predicted to churn.")
        
        st.write(f"Prediction Probability: {probability * 100:.2f}%")
