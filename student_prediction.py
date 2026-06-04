import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("student_performance.csv")

X = data[["Study_Hours", "Attendance", "Previous_Score"]]
y = data["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
<<<<<<< HEAD
print("Model Accuracy:", accuracy_score(y_test, y_pred))
=======

print("Accuracy:", accuracy_score(y_test, y_pred))
>>>>>>> 6d4dbb5e160bd5ff7a2d7de33d7017839b75413d

study_hours = int(input("Enter study hours: "))
attendance = int(input("Enter attendance: "))
previous_score = int(input("Enter previous score: "))

<<<<<<< HEAD
new_data = pd.DataFrame([[study_hours, attendance, previous_score]],
                        columns=["Study_Hours", "Attendance", "Previous_Score"])

prediction = model.predict(new_data)

print("Prediction:", prediction[0])
=======
prediction = model.predict([[study_hours, attendance, previous_score]])

print("Prediction:", prediction[0])
>>>>>>> 6d4dbb5e160bd5ff7a2d7de33d7017839b75413d
