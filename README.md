Project Overview

  1. Customer Churn Prediction System is a machine learning-based web application to predict if a customer will discontinue telecom services.
     
  2. It uses a Random Forest Classifier trained on a telecom dataset.

  3. SMOTE is used to address class imbalance by oversampling the minority class.

  4. The app helps telecom companies identify high-risk customers and take proactive retention actions.

  5. Developed using Python, scikit-learn, and Streamlit for the web interface.

     

Problem Statement

  1. Customer retention is more cost-effective than acquiring new customers.

  2. Predicting churn is complex due to diverse customer behavior patterns.

  3. Machine learning is used to detect churn patterns from data.

  4. A user-friendly interface enables real-time prediction access.

  5. SMOTE balances the dataset to improve prediction fairness.
     

Project Goals

  1. Predict customer churn likelihood using a trained ML model.

  2. Provide real-time prediction through a web interface.

  3. Present interpretable results to help business users.


Project Architecture

  1. Dataset used is tel_churn.csv. Data includes demographics, account details, services, and billing information.

  2. Target variable is Churn, represented as Yes or No. Data preprocessing includes handling missing values and encoding features.

  3. SMOTE is applied to balance churn vs non-churn classes. Random Forest Classifier is trained using scikit-learn.

  4. Model is saved as model_rf_smote.sav using pickle. Web interface is built with Streamlit (app.py).

  5. Interface accepts user inputs through widgets like dropdowns and number inputs. Inputs include demographics, billing, services used, contract type, and payment method.

  6. Inputs are one-hot encoded to match training format. Model is loaded and used to predict churn (0 or 1).

  7. Probability score is displayed along with prediction. Logging is implemented using Python’s logging module. Logs are saved in streamlit_app.log.


Key Features

  1. Predicts churn using a trained Random Forest model.

  2. Provides real-time prediction based on user inputs.

  3. Uses Streamlit for interactive and user-friendly interface.

  4. Ensures data is formatted correctly for the model using one-hot encoding.

  5. Logs all model activity and errors for debugging.


Input Parameters

  1. Gender

  2. Senior Citizen status

  3. Partner

  4. Dependents

  5. Phone Service

  6. Internet Service

  7. Multiple Lines

  8. Online Security

  9. Online Backup

  10. Device Protection

  11. Tech Support

  12. Streaming TV

  13. Streaming Movies

  14. Monthly Charges

  15. Total Charges

  16. Contract Type

  17. Paperless Billing

  18. Payment Method

  19. Tenure Group


Model Output

  1. Churn prediction as 0 (Stay) or 1 (Churn)

  2. Probability score between 0.0 and 1.0 indicating confidence

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a10d81d0-e66a-40b0-ad40-e2f2abc88395" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/1b2c9d91-2ab4-473d-bb92-a8777bda0efd" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a5a53154-5280-491f-9a05-f11c4af3b7fc" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/396608fe-6983-4c3a-ae7e-1d4e314f57a7" />
