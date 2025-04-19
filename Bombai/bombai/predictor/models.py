import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Dummy dataset
data = {
    "gpa": [2.5, 3.0, 2.0, 1.8, 3.5, 1.5],
    "attendance": [80, 90, 60, 50, 95, 45],
    "income": [30000, 50000, 20000, 15000, 60000, 10000],
    "support": [1, 1, 0, 0, 1, 0],
    "mental_health": [7, 8, 4, 3, 9, 2],
    "activities": [1, 1, 0, 0, 1, 0],
    "materials": [1, 1, 0, 0, 1, 0],
    "mode": [0, 1, 0, 0, 2, 0],
    "dropout": [0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Split dataset
X = df.drop("dropout", axis=1)
y = df["dropout"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model to predictor/models/model.pkl
os.makedirs("predictor/models", exist_ok=True)
joblib.dump(model, "predictor/models/model.pkl")
