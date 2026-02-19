import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

data_path = "database/attendance_data.csv"
df = pd.read_csv(data_path)

X = df[["total_classes", "attended_classes", "subject_difficulty"]]
y = df["detained_risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/attendance_model.pkl")

print("\nModel saved successfully as model/attendance_model.pkl")
