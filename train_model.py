import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load and clean CSV
data = pd.read_csv("bpm_dataset.csv")

# Drop rows with BPM outside a reasonable range
data = data[(data['bpm'] >= 30) & (data['bpm'] <= 200)]

# Encode activity labels
label_map = {'rest': 0, 'walk': 1, 'run': 2}
data['activity'] = data['activity'].map(label_map)

# Separate features and labels
X = data[['bpm']]
y = data['activity']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model (KNN)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, "bpm_activity_model.pkl")
print("\nModel saved to bpm_activity_model.pkl")
