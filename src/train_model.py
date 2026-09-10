import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/students_placement.csv")

X = df.drop("Placement_Status", axis=1)
y = df["Placement_Status"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

joblib.dump(model, "src/placement_model.pkl")
joblib.dump(X.columns.tolist(), "src/model_columns.pkl")

print("Model Training Completed!")
print("Accuracy:", accuracy)
print("Model Saved Successfully!")