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

# Footer
st.markdown("---")

st.caption("Built by Alina | AI & Data Analytics Capstone Project")