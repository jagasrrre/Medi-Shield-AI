import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

def train_anomaly_detector():
    # Load the hospital security logs
    df = pd.read_csv("hospital_logs.csv")  # Replace with actual log data source

    # Drop missing values
    df.dropna(inplace=True)

    # Convert categorical values (if any)
    df = pd.get_dummies(df, drop_first=True)

    # Normalize numerical data
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    # Train Isolation Forest model
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df_scaled)

    # Save model
    joblib.dump((model, scaler), "anomaly_detector.pkl")
    print("Model trained and saved successfully!")

# Train model when script is run
if __name__ == "__main__":
    train_anomaly_detector()
