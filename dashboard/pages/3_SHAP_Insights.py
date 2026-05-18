import streamlit as st

st.title("🧠 SHAP Explainable AI")

st.write("""
SHAP explains why the model predicts fraud.
It helps analysts understand feature importance.
""")

st.image(
    "dashboard/shap_summary.png",
    caption="SHAP Global Feature Importance"
)

st.success("Explainable AI loaded successfully")