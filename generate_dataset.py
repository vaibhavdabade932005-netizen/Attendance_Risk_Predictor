import pandas as pd
import random

data = []

for _ in range(500):
    total_classes = random.randint(60, 150)
    attended_classes = random.randint(0, total_classes)

    subject_difficulty = random.randint(1, 3)

    attendance_percentage = (attended_classes / total_classes) * 100
    detained_risk = 1 if attendance_percentage < 75 else 0

    data.append([total_classes, attended_classes, subject_difficulty, detained_risk])

df = pd.DataFrame(data, columns=[
    "total_classes", "attended_classes", "subject_difficulty", "detained_risk"
])

df.to_csv("database/attendance_data.csv", index=False)

print("New dataset created successfully with 500 rows!")
