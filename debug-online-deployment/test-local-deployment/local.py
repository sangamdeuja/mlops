# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Score.py for serving the trained model as an HTTP web service.
"""
import os
import json
import joblib
import numpy as np

def init():
    """
    Initialize the model for inference.
    This is run once during the deployment initialization.
    """
    global model
    model_path = "mlmodel/model.pkl"
    model = joblib.load(model_path)

def run(data):
    data=json.loads(data)["data"]
    data=np.array(data)
    pred = model.predict(data)
    return pred.tolist()