import os
import joblib
import numpy as np

model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), './model.bin')

def init():
    """
    This method is used by the Azure Machine Learning Service to initialize
    the scoring script. Modify this method to suit your model's needs.
    """
    global model, model_path
    model = joblib.load(model_path)

def run(data):
    """
    This method is used by Azure Machine Learning Service to make predictions.
    Modify this method to suit your model's needs.
    """
    global model

    output = model.predict(np.array(data))

    return output