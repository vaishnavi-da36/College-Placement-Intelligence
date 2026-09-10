import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_students_placement.csv")

# Basic dataset information
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Placement status count
print("\nPlacement Status:")
print(df["Placement_Status"].value_counts())

# Department-wise student count
print("\nDepartment-wise Student Count:")
print(df["Department"].value_counts())

# Average CGPA
print("\nAverage CGPA:", df["CGPA"].mean())

# Average Aptitude Score
print("\nAverage Aptitude Score:", df["Aptitude_Score"].mean())

# Average Coding Score
print("\nAverage Coding Score:", df["Coding_Score"].mean())