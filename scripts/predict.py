import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv('../data/solar_power_data.csv')
X = data.drop(columns=['failure_status'])
y = data['failure_status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save model
joblib.dump(model, '../models/predictive_maintenance_model.pkl')
print("Model trained and saved to models/predictive_maintenance_model.pkl")
