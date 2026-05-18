import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Fraud Analytics Overview")

# Sample metrics
total_transactions = 590000
fraud_count = 20663
fraud_rate = (fraud_count / total_transactions) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", f"{total_transactions:,}")
col2.metric("Fraud Cases", f"{fraud_count:,}")
col3.metric("Fraud Rate", f"{fraud_rate:.2f}%")

# Sample chart
risk_df = pd.DataFrame({
    "Risk": ["Safe", "Suspicious", "Critical"],
    "Count": [520000, 50000, 20000]
})

fig = px.pie(
    risk_df,
    names="Risk",
    values="Count",
    hole=0.5,
    title="Risk Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Overview analysis completed")