import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("placement-placement.pkl", "rb"))
st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎓",
    layout="centered"
)
st.title("Student Placement Prediction")
st.write("Enter student details to predict placement status.")
CGPA = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.5,
    step=0.1
)
Internships = st.number_input(
    "Number of Internships",
    min_value=0,
    max_value=10,
    value=1
)
Projects = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=10,
    value=2
)
Workshops = st.number_input(
    "Workshops/Certifications",
    min_value=0,
    max_value=10,
    value=2
)

AptitudeTestScore = st.number_input(
    "Aptitude Test Score",
    min_value=0,
    max_value=100,
    value=75
)

SoftSkillsRating = st.number_input(
    "Soft Skills Rating",
    min_value=0.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

ExtracurricularActivities = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

PlacementTraining = st.selectbox(
    "Placement Training",
    ["No", "Yes"]
)

SSC_Marks = st.number_input(
    "SSC Marks",
    min_value=0,
    max_value=100,
    value=70
)

HSC_Marks = st.number_input(
    "HSC Marks",
    min_value=0,
    max_value=100,
    value=75
)
ExtracurricularActivities = (
    1 if ExtracurricularActivities == "Yes" else 0
)

PlacementTraining = (
    1 if PlacementTraining == "Yes" else 0
)
if st.button("Predict Placement"):
    input_data = np.array([[
        CGPA,
        Internships,
        Projects,
        Workshops,
        AptitudeTestScore,
        SoftSkillsRating,
        ExtracurricularActivities,
        PlacementTraining,
        SSC_Marks,
        HSC_Marks
    ]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Student is likely to be PLACED!")
    else:
        st.error("Student is likely to be NOT PLACED.")

