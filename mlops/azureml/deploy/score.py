# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Score.py for serving the trained model as an HTTP web service.
"""
import os
import json
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Global variable to hold the model
model = None

def init():
    """
    Initialize the model for inference.
    This is run once during the deployment initialization.
    """
    global model
    model_path = os.path.join(os.environ.get("AZUREML_MODEL_DIR"), "taxi-model.pkl")
    model = joblib.load(model_path)

def run(input_data: str):
    """
    Run inference on the input data.
    This function is invoked for each HTTP request.
    """
    global model
    try:
        # Parse the input JSON data
        input_json = json.loads(input_data)

        # Convert input data to pandas DataFrame
        # Assume the input JSON is an array of data points
        input_df = pd.DataFrame(input_json)

        # Ensure the model expects the correct input columns
        required_columns = [
            "distance", "dropoff_latitude", "dropoff_longitude", "passengers", 
            "pickup_latitude", "pickup_longitude", "pickup_weekday", "pickup_month",
            "pickup_monthday", "pickup_hour", "pickup_minute", "pickup_second", 
            "dropoff_weekday", "dropoff_month", "dropoff_monthday", "dropoff_hour", 
            "dropoff_minute", "dropoff_second"
        ]
        
        # Check if the input contains all necessary columns
        missing_columns = [col for col in required_columns if col not in input_df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

        # Make predictions
        predictions = model.predict(input_df)

        # Return the predictions as a JSON response
        response = {
            "predictions": predictions.tolist()
        }

        return json.dumps(response)

    except Exception as e:
        error_message = f"Error in prediction: {str(e)}"
        print(error_message)
        return json.dumps({"error": error_message})
