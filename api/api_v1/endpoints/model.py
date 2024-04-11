import json
import pandas as pd
import numpy as np
from pycaret.regression import predict_model, load_model

model = load_model('squamish-pipeline')

def setup_data(input_data):
    # Convert all data types to native Python types
    # input_data = {key: [value] for key, value in input_data.items()}
    data = pd.DataFrame(input_data, index=[0])

    # Convert all columns to native Python types
    for col in data.columns:
        data[col] = data[col].astype(np.float64) if np.issubdtype(data[col].dtype, np.number) else data[col]

    return data

"""
Make a prediction with the model.
:param data: A pandas DataFrame with the input data.
"""
def use_model(input_data):
    data = setup_data(input_data)
    predictions = predict_model(model, data)
    # Change predictions from numpy array to list
    json_data = predictions.to_json(orient='index')
    json_data = json.loads(json_data)
    return json_data
