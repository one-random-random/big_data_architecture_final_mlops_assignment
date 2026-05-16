from flask import Flask, request
from joblib import load
import numpy as np
from pathlib import Path

from constants import MODEL_FILE_NAME

project_root = Path(__file__).resolve().parent.parent
model_path = project_root / "models" / MODEL_FILE_NAME

app = Flask(__name__)
model = load(model_path)

@app.route('/')
def welcome():
    return "Hello and welcome to my Salary Prediction app."

@app.route('/health')
def health_check():
    return {"status": "healthy"}, 200

@app.route('/predict')
def predict_salary():
    experience = request.args.get('experience')

    if experience is None:
        return "Missing required query parameter: experience", 400

    try:
        years_experience = float(experience)
    except ValueError:
        return "Query parameter 'experience' must be a number", 400

    prediction = model.predict([[years_experience]])
    rounded_prediction = np.round(prediction[0], 2)
    
    return f"The predicted salary based on {experience} years of experience is: {rounded_prediction}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
