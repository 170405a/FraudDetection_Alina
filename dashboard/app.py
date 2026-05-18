import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("dashboard/model.pkl")

# Page settings
st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="🚨"
)

st.title("Real-Time Fraud Detection System")

st.write("Fraud Prediction Dashboard")

# Sidebar
st.sidebar.header("Transaction Details")

amount = st.sidebar.number_input(
    "Transaction Amount",
    value=100.0
)

hour = st.sidebar.slider(
    "Hour of Transaction",
    0,
    23,
    12
)

# Input dataframe
input_data = pd.DataFrame({
    "TransactionAmt": [amount],
    "HourOfDay": [hour]
})

# Prediction
if st.button("Predict Fraud Risk"):

    prob = model.predict_proba(input_data)[0][1]

    st.write("Fraud Probability:", round(prob, 4))

    if prob >= 0.75:
        st.error("Critical Risk Transaction")

    elif prob >= 0.40:
        st.warning("Suspicious Transaction")

    else:
        st.success(" Safe Transaction")