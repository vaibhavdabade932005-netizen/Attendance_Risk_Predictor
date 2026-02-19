import streamlit as st
import joblib
import os
import math

st.subheader("📌 75% Attendance Calculator")

total_sem_classes = st.number_input(
    "Total Classes in Semester (for 1 subject)", 
    min_value=1, 
    value=70
)

min_required = math.ceil(0.75 * total_sem_classes)

st.info(
    f"✅ Minimum classes required for 75% attendance: **{min_required}** out of **{total_sem_classes}**"
)

model_path = "model/attendance_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found! Please run train_model.py first.")
else:
    model = joblib.load(model_path)

    st.title("📌 Student Attendance Risk Predictor")
    st.write("This app predicts whether a student is at risk of detention based on attendance details.")

    st.subheader("Enter Student Details:")

    total_classes = st.number_input("Total Classes", min_value=1, value=100)
    attended_classes = st.number_input("Attended Classes", min_value=0, value=70)

    subject_difficulty = st.selectbox(
        "Subject Difficulty",
        options=[1, 2, 3],
        format_func=lambda x: "Easy" if x == 1 else "Medium" if x == 2 else "Hard"
    )

    if attended_classes > total_classes:
        st.warning("Attended classes cannot be more than total classes!")

    if st.button("Predict Risk"):
        input_data = [[total_classes, attended_classes, subject_difficulty]]

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][prediction] * 100

        attendance_percentage = (attended_classes / total_classes) * 100

        st.write(f"📊 Attendance Percentage: **{attendance_percentage:.2f}%**")

        if prediction == 1:
            st.error(f"❌ High Detention Risk! (Confidence: {probability:.2f}%)")
        else:
            st.success(f"✅ Safe Attendance Level (Confidence: {probability:.2f}%)")
