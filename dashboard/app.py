import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="🚨",
    layout="wide"
)

# Load model
model = joblib.load("dashboard/model.pkl")

# Title
st.title("🚨 Real-Time Fraud Detection System")

st.markdown("""
This dashboard predicts fraudulent financial transactions using Machine Learning.
""")

# Sidebar
st.sidebar.header("Transaction Input")

amount = st.sidebar.number_input(
    "Transaction Amount",
    min_value=1.0,
    value=100.0
)

hour = st.sidebar.slider(
    "Hour Of Day",
    0,
    23,
    12
)

# Create dataframe
input_data = pd.DataFrame({
    "TransactionAmt": [amount],
    "HourOfDay": [hour]
})

# Predict
if st.button("Predict Fraud Risk"):

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.metric(
        label="Fraud Probability",
        value=f"{probability:.2%}"
    )

    # Risk categories
    if probability >= 0.75:
        risk = "Critical Risk"
        st.error("🔴 Critical Risk Transaction")

    elif probability >= 0.40:
        risk = "Suspicious"
        st.warning("🟡 Suspicious Transaction")

    else:
        risk = "Safe"
        st.success("🟢 Safe Transaction")

    # Risk dataframe
    chart_df = pd.DataFrame({
        "Risk Category": ["Safe", "Suspicious", "Critical"],
        "Value": [1-probability, probability/2, probability/2]
    })

    # Plotly donut chart
    fig = px.pie(
        chart_df,
        names="Risk Category",
        values="Value",
        hole=0.5,
        title="Fraud Risk Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
# ==============================
# CSV Upload Fraud Detection
# ==============================

st.subheader("📂 Upload Transactions CSV")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    upload_df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data Preview")

    st.dataframe(upload_df.head())

    # Check required columns
    required_cols = ["TransactionAmt", "HourOfDay"]

    if all(col in upload_df.columns for col in required_cols):

        # Predict probabilities
        fraud_probs = model.predict_proba(
            upload_df[required_cols]
        )[:, 1]

        upload_df["FraudProbability"] = fraud_probs

        # Risk tier
        def risk_label(prob):

            if prob >= 0.75:
                return "Critical"

            elif prob >= 0.40:
                return "Suspicious"

            else:
                return "Safe"

        upload_df["RiskLevel"] = upload_df[
            "FraudProbability"
        ].apply(risk_label)

        st.subheader("Prediction Results")

        st.dataframe(upload_df.head())

    else:

        st.error(
            "CSV must contain TransactionAmt and HourOfDay columns"
        )
# Footer
st.markdown("---")

st.caption("Built by Alina | AI & Data Analytics Capstone Project")