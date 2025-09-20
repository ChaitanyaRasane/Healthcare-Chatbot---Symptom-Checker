import streamlit as st
from model import SymptomCheckerModel
from utils import description_dict, precaution_dict, assess_severity

st.set_page_config(page_title="Symptom Checker", layout="centered")
st.title("🤖 Healthcare Chatbot - Symptom Checker")

model = SymptomCheckerModel()

symptom_input = st.text_input("Enter your symptoms (comma-separated):", "")
days = st.slider("How many days have you experienced these symptoms?", 1, 30, 3)

if st.button("Check Disease"):
    symptoms = [s.strip().replace(' ', '_') for s in symptom_input.split(',') if s.strip()]
    
    if symptoms:
        disease = model.predict(symptoms)
        st.success(f"You may have: **{disease}**")

        desc = description_dict.get(disease, "No description available.")
        st.info(f"🩺 *{desc}*")

        st.warning(assess_severity(symptoms, days))

        precautions = precaution_dict.get(disease, [])
        if precautions:
            st.markdown("### ✅ Precautionary Measures")
            for i, p in enumerate(precautions):
                st.markdown(f"- {p}")
    else:
        st.error("Please enter at least one symptom.")



# st.markdown("### 🎙️ Voice Input")

# if st.button("🎤 Speak Symptoms"):
#     with st.spinner("Listening..."):
#         voice_symptoms = listen()
#         if voice_symptoms:
#             st.success(f"You said: **{voice_symptoms}**")
#             symptom_input = voice_symptoms
#         else:
#             st.error("Could not understand. Please try again.")
