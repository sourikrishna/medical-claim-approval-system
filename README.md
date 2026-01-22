# 🏥 Medical Insurance Claim Approval System

An end-to-end **Machine Learning web application** that predicts:
- ✅ Whether a medical insurance claim will be **approved**
- 💰 The **approved payout amount** (if approved)

The application is fully **deployed and publicly accessible** using Streamlit Cloud.

---

## 🌐 Live Application
🔗 https://medical-claim-approval-system-emszxk9rwdfyibrqwftexe.streamlit.app/

---

## 📌 About the Project
Medical insurance companies handle a large number of claims every day.  
Manual evaluation is time-consuming, inconsistent, and costly.

🎯 This project automates:
- Claim approval decision
- Approved payout estimation  
using **Machine Learning models**, simulating a real-world insurance workflow.

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository
git clone https://github.com/sourikrishna/medical-claim-approval-system.git
cd medical-claim-approval-system


---

### 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate


---

### 3️⃣ Install dependencies
pip install -r requirements.txt


---

### 4️⃣ Run the application
streamlit run app/streamlit_app.py


---

### 5️⃣ Open in browser
http://localhost:8501


---

## 🧠 Machine Learning Workflow

### 🔹 Claim Approval Model (Classification)
- Predicts whether a claim is approved or rejected
- Outputs an approval probability score

### 🔹 Approved Amount Model (Regression)
- Runs only if the claim is approved
- Predicts the final payable amount

---

## 📁 Folder Structure

medical-claim-approval-system/
|
|-- app/
| |-- streamlit_app.py # Streamlit web application
|
|-- data/
| |-- raw/
| |-- medical_claims.csv # Synthetic dataset
|
|-- models/
| |-- approval_model.pkl # Trained approval model
| |-- amount_model.pkl # Trained payout model
|
|-- notebooks/
| |-- 01_eda.ipynb # Exploratory Data Analysis
|
|-- requirements.txt # Project dependencies
|-- .gitignore
|-- README.md


---

## 📊 Dataset Information
- Synthetic dataset (privacy-safe)
- Designed to simulate real medical insurance claims
- Features include:
  - Age & gender
  - Policy type & sum insured
  - Hospital type
  - Disease category
  - Claimed amount
  - Length of hospital stay
  - Previous claims history

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- Git & GitHub

---

## ✨ Key Features
- Interactive web interface
- Approval probability display
- Payable amount prediction
- Robust feature alignment for production
- Fully deployed ML system

---

## 🚀 Deployment
- Deployed on **Streamlit Cloud**
- GitHub-integrated CI/CD
- Dependency management using `requirements.txt`

---

## 🔮 Future Enhancements
- Explainable AI (SHAP)
- Claim rejection reasoning
- Downloadable PDF claim reports
- Authentication & access control
- Cloud deployment on AWS / Azure

---

## 👤 Author
**Souri Krishna**  
Aspiring Data Scientist 
