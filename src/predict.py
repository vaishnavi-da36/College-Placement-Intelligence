import pandas as pd
import joblib

# Load trained model
model = joblib.load("src/placement_model.pkl")
model_columns = joblib.load("src/model_columns.pkl")

# Student details
student = pd.DataFrame([{
    "Department": "AI & DS",
    "CGPA": 8.5,
    "Tenth_Percentage": 85,
    "Twelfth_Percentage": 88,
    "Aptitude_Score": 75,
    "Coding_Score": 80,
    "Communication_Score": 78,
    "Internship": "Yes",
    "Certifications": 3,
    "Projects_Count": 3,
    "Attendance_Percentage": 90,
    "Backlogs": 0
}])

# Convert categorical columns
student = pd.get_dummies(student, drop_first=True)

# Match training columns
student = student.reindex(columns=model_columns, fill_value=0)

# Predict
prediction = model.predict(student)[0]

# Get probability
probabilities = model.predict_proba(student)[0]
class_names = model.classes_

placement_probability = probabilities[
    list(class_names).index("Placed")
] * 100

print("Student Placement Prediction:", prediction)
print("Placement Probability:", round(placement_probability, 2), "%")