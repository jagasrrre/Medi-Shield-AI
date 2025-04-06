import pandas as pd
import joblib
from django.shortcuts import render
from django.http import JsonResponse



# Load trained model
model, scaler = joblib.load("anomaly_detector.pkl")

def detect_anomalies(request):
    if request.method == "POST":
        file = request.FILES["log_file"]

        # Read CSV file
        df = pd.read_csv(file)

        # Preprocess data
        df.dropna(inplace=True)
        df = pd.get_dummies(df, drop_first=True)
        df_scaled = scaler.transform(df)

        # Predict anomalies
        df["Anomaly"] = model.predict(df_scaled)
        df["Anomaly"] = df["Anomaly"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

        return JsonResponse({"data": df.to_dict(orient="records")})

    return render(request, "detect_anomalies.html")
