import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Medical Insurance Claim System",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Glass container using Streamlit native blocks */
[data-testid="stVerticalBlock"] {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
}

/* Button styling */
.stButton > button {
    background: rgba(255, 255, 255, 0.25);
    color: white;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 0.6em 1.2em;
    font-weight: bold;
}
.stButton > button:hover {
    background: rgba(255, 255, 255, 0.4);
}

/* Labels */
label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

approval_model = joblib.load(os.path.join(BASE_DIR, "models", "approval_model.pkl"))
amount_model = joblib.load(os.path.join(BASE_DIR, "models", "amount_model.pkl"))

st.title("🏥 Medical Insurance Claim Decision System")
st.write("Enter claim details to check approval and payable amount")

with st.container():
    st.subheader("📋 Claim Details")

    age = st.slider("Age", 18, 80, 35)
    gender = st.selectbox("Gender", ["Male", "Female"])
    policy_type = st.selectbox("Policy Type", ["Basic", "Premium", "Gold"])
    sum_insured = st.selectbox("Sum Insured", [200000, 300000, 500000, 1000000])
    disease_category = st.selectbox(
        "Disease Category", ["Cardiac", "Orthopedic", "Cancer", "General"]
    )
    hospital_type = st.selectbox("Hospital Type", ["Network", "Non-Network"])
    length_of_stay = st.slider("Length of Stay (days)", 1, 30, 5)
    claimed_amount = st.number_input("Claimed Amount", 10000, 500000, 50000)
    previous_claims = st.slider("Previous Claims", 0, 5, 0)

# -------------------- PREDICTION --------------------
if st.button("Predict Claim Decision"):

    raw_input = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "policy_type": [policy_type],
        "sum_insured": [sum_insured],
        "disease_category": [disease_category],
        "hospital_type": [hospital_type],
        "length_of_stay": [length_of_stay],
        "claimed_amount": [claimed_amount],
        "previous_claims": [previous_claims]
    })

    encoded_input = pd.get_dummies(raw_input, drop_first=True)

    # -------- APPROVAL MODEL --------
    approval_features = approval_model.feature_names_in_
    approval_input = encoded_input.reindex(columns=approval_features, fill_value=0)

    approval_prob = approval_model.predict_proba(approval_input)[0][1]
    approved = approval_prob >= 0.5

    with st.container():
        if approved:
            amount_features = amount_model.feature_names_in_
            amount_input = encoded_input.reindex(columns=amount_features, fill_value=0)
            approved_amount = amount_model.predict(amount_input)[0]

            st.success(f"✅ Claim Approved (Probability: {approval_prob:.2f})")
            st.info(f"💰 Approved Amount: ₹{int(approved_amount)}")

        else:
            st.error(f"❌ Claim Rejected (Probability: {approval_prob:.2f})")
