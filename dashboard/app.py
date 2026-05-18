import streamlit as st

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Real-Time Fraud Detection System")

st.markdown("""
Welcome to the AI-powered Fraud Detection Dashboard.

Use the sidebar to navigate between pages.
""")

st.image(
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
    use_container_width=True
)

st.markdown("---")

st.subheader("Project Features")

st.write("""
✅ Real-Time Fraud Prediction  
✅ Machine Learning Models  
✅ Risk Segmentation  
✅ Explainable AI using SHAP  
✅ CSV Upload Analysis  
✅ Interactive Visualizations  
""")

st.success("System Ready")