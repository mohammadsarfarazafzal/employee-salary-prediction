import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Employee Salary Prediction", layout="centered")

model = joblib.load("salary_prediction_model.joblib")

st.markdown("## 🎯 Predict Employee Salary")
st.markdown("Enter the employee details below:")

with st.form("predict_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=70, value=30)
        experience = st.slider("Years of Experience", 0, 50, 5)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
        education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
        job = st.selectbox("Job Title", ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"])

    submitted = st.form_submit_button("💰 Predict Salary")

if submitted:
    try:
        input_df = pd.DataFrame([{
            "Age": age,
            "Gender": gender,
            "Education Level": education,
            "Job Title": job,
            "Years of Experience": experience
        }])
        prediction = model.predict(input_df)[0]
        st.success(f"🤑 Estimated Salary: **${int(prediction):,}**")
        st.balloons()
    except Exception as e:
        st.error(f"Something went wrong: {e}")
