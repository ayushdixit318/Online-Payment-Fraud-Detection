from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize Flask app
app = Flask(__name__)

# Home route with form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Collect user inputs from the form
    inputs = [
        float(request.form['step']),
        float(request.form['type']),
        float(request.form['amount']),
        float(request.form['oldbalanceOrg']),
        float(request.form['oldbalanceDest']),
    ]

    # Scale the inputs
    scaled_inputs = scaler.transform([inputs])

    # Make a prediction
    prediction = model.predict(scaled_inputs)[0]

    # Map prediction to human-readable output
    result = "Fraudulent" if prediction == 1 else "Non-Fraudulent"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
