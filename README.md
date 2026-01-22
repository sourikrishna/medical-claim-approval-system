# Medical Insurance Claim Approval System

An end-to-end machine learning application that predicts:
1. Whether a medical insurance claim will be approved
2. The approved payout amount (if approved)

The project is fully deployed as a web application using Streamlit Cloud.

--------------------------------------------------

LIVE DEMO
Live URL: [https://medical-claim-approval-system.streamlit.app](https://medical-claim-approval-system-emszxk9rwdfyibrqwftexe.streamlit.app/)

--------------------------------------------------

PROBLEM STATEMENT
Medical insurance companies must evaluate claims efficiently while minimizing risk and financial loss.
This project automates the claim decision process using machine learning to:
- Predict claim approval (Yes / No)
- Estimate the payable amount for approved claims

--------------------------------------------------

SOLUTION OVERVIEW
The system uses a two-stage machine learning pipeline:

1) Claim Approval Model (Classification)
- Predicts whether a claim should be approved
- Outputs approval probability

2) Approved Amount Model (Regression)
- Runs only if the claim is approved
- Predicts the payable amount

This design mirrors real-world insurance workflows.

--------------------------------------------------

PROJECT STRUCTURE

medical-claim-approval-system/
|
|-- app/
|   |-- streamlit_app.py        (Streamlit web application)
|
|-- data/
|   |-- raw/medical_claims.csv  (Synthetic dataset)
|
|-- models/
|   |-- approval_model.pkl      (Trained approval model)
|   |-- amount_model.pkl        (Trained payout model)
|
|-- notebooks/
|   |-- 01_eda.ipynb            (Exploratory Data Analysis)
|
|-- requirements.txt
|-- .gitignore
|-- README.md

--------------------------------------------------

DATASET
- The dataset is synthetically generated
- Designed to simulate real-world medical insurance claims
- Includes:
  - Policy details
  - Hospital type
  - Disease category
  - Claim amount
  - Claim history

Synthetic data is used due to privacy and regulatory constraints in healthcare.

--------------------------------------------------

TECHNOLOGIES USED
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- Git & GitHub

--------------------------------------------------

MACHINE LEARNING MODELS
- Logistic Regression (baseline)
- Random Forest / XGBoost (final models)
- Separate feature alignment for production inference

--------------------------------------------------

KEY FEATURES
- Interactive web interface
- Approval probability display
- Payable amount estimation
- Robust feature handling during deployment
- Production-grade model loading

--------------------------------------------------

DEPLOYMENT
The application is deployed using:
- Streamlit Cloud
- GitHub integration
- Dependency management via requirements.txt

--------------------------------------------------

HOW TO RUN LOCALLY

```bash
git clone https://github.com/<your-username>/medical-claim-approval-system.git
cd medical-claim-approval-system
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py

--------------------------------------------------

FUTURE ENHANCEMENTS
- Explainable AI (SHAP)
- Claim rejection reasons
- PDF claim report generation
- Authentication and role-based access
- Cloud deployment on AWS or Azure

--------------------------------------------------

AUTHOR
Souri Krishna  
Aspiring Data Scientist

--------------------------------------------------

