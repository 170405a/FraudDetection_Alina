import streamlit as st
import pandas as pd
import joblib

st.title("🔍 Transaction Explorer")

model = joblib.load("dashboard/model.pkl")

uploaded_file = st.file_uploader(
    "Upload Transaction CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Transactions")

    st.dataframe(df.head())

    required_cols = ["TransactionAmt", "HourOfDay"]

    if all(col in df.columns for col in required_cols):

        probs = model.predict_proba(
            df[required_cols]
        )[:, 1]

        df["FraudProbability"] = probs

        st.subheader("Prediction Results")

        st.dataframe(df)

    else:

        st.error(
            "CSV must contain TransactionAmt and HourOfDay"
        )