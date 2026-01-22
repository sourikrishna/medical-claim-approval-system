# 🏥 Medical Insurance Claim Approval System

An end-to-end **Machine Learning web application** that predicts:
- ✅ Whether a medical insurance claim will be approved
- 💰 The approved payout amount (if approved)

The application is fully deployed using **Streamlit Cloud**.

---

## 🌐 Live Application
https://medical-claim-approval-system-emszxk9rwdfyibrqwftexe.streamlit.app/

---

## 📌 About the Project
Medical insurance companies process a large number of claims every day.  
Manual evaluation is time-consuming and error-prone.

This project automates:
- Claim approval decisions
- Approved payout estimation  

using Machine Learning models that simulate real-world insurance workflows.

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/sourikrishna/medical-claim-approval-system.git
cd medical-claim-approval-system
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run app/streamlit_app.py
```

### 5. Open in browser
```
http://localhost:8501
```

---

## 🧠 Machine Learning Workflow

### Claim Approval Model (Classification)
- Predicts approval or rejection
- Outputs approval probability

### Approved Amount Model (Regression)
- Runs only if the claim is approved
- Predicts the final payable amount

---

## 📁 Folder Structure

```
medical-claim-approval-system/
|
|-- app/
|   |-- streamlit_app.py          # Streamlit web application
|
|-- data/
|   |-- raw/
|       |-- medical_claims.csv    # Synthetic dataset
|
|-- models/
|   |-- approval_model.pkl        # Trained approval model
|   |-- amount_model.pkl          # Trained payout model
|
|-- notebooks/
|   |-- 01_eda.ipynb              # Exploratory Data Analysis
|
|-- requirements.txt              # Project dependencies
|-- .gitignore
|-- README.md
```

---

## 📊 Dataset Information
- Synthetic dataset (privacy-safe)
- Simulates real medical insurance claims
- Includes age, gender, policy type, hospital type, disease category,
  claimed amount, length of stay, and previous claims

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- Git & GitHub

---

## 🚀 Deployment
The application is deployed using:
- Streamlit Cloud
- GitHub integration
- Dependency management via requirements.txt

---

## 🔮 Future Enhancements
- Explainable AI (SHAP)
- Claim rejection reasons
- PDF claim report generation
- Authentication and role-based access
- Cloud deployment on AWS or Azure

---

## 👤 Author
Souri Krishna  
Aspiring Data Scientist
