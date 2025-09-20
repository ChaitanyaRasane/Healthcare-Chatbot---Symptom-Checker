import csv

def load_csv_to_dict(filepath):
    with open(filepath) as file:
        reader = csv.reader(file)
        result = {}
        for row in reader:
            if len(row) >= 2:
                result[row[0]] = row[1:] if len(row) > 2 else row[1]
        return result

severity_dict = load_csv_to_dict('MasterData/Symptom_severity.csv')
description_dict = load_csv_to_dict('MasterData/symptom_Description.csv')
precaution_dict = load_csv_to_dict('MasterData/symptom_precaution.csv')

def assess_severity(symptoms, days):
    total = sum(int(severity_dict.get(symptom, 0)) for symptom in symptoms)
    level = (total * days) / (len(symptoms) + 1)
    if level > 13:
        return "⚠️ You should consult a doctor."
    else:
        return "🩺 It's likely not serious, but precautions are advised."

# import pyttsx3
# import speech_recognition as sr

# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 130)
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()
#     with mic as source:
#         print("Listening for symptoms...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     try:
#         command = recognizer.recognize_google(audio)
#         return command
#     except sr.UnknownValueError:
#         return ""
#     except sr.RequestError:
#         return ""
