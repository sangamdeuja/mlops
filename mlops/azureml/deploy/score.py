# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Score.py for serving the trained model as an HTTP web service.
"""
import os
import json
import joblib
import numpy as np

# Global variable to hold the model
def init():
    """
    Initialize the model for inference.
    This is run once during the deployment initialization.
    """
    global model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "taxi-model", "model.pkl")
    model = joblib.load(model_path)

def run(input_data: str):
    """
    Run inference on the input data.
    This function is invoked for each HTTP request.
    """
    data=json.loads(input_data)
    data=np.array(data)
    prediction=model.predict(data)
    response = {
            "predictions": prediction.tolist()
        }
    return response
   
   

