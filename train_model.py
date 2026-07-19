import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Create 'model' folder if it doesn't exist
model_dir = 'model'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Step 2: Load the dataset
data = pd.read_csv('Crop_recommendation.csv')

# Step 3: Select the required columns
X = data[['soil_ph', 'temperature', 'humidity', 'soil_moisture']]
y = data['crop']

# Step 4: Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Step 6: Train Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Step 7: Choose the better model (based on test accuracy, but not printed)
rf_accuracy = accuracy_score(y_test, rf_model.predict(X_test))
dt_accuracy = accuracy_score(y_test, dt_model.predict(X_test))

best_model = rf_model if rf_accuracy >= dt_accuracy else dt_model

# Step 8: Save the selected model
model_path = os.path.join(model_dir, 'crop_prediction_model.pkl')
joblib.dump(best_model, model_path)

print(f"✅ Model trained and saved successfully at {model_path}")
