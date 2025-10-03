from flask import Flask, render_template, request
import pickle
import numpy as np
<<<<<<< HEAD

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
=======
import os

app = Flask(__name__)

# Load trained model
try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
>>>>>>> d3b765688500478c8fd09abf46b83e973ba3ad35

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
<<<<<<< HEAD
    try:
        features = [float(x) for x in request.form.values()]
        while len(features) <13:
            features.append(0.0)
        final_features = np.array([features])
        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = 'High Risk of Heart Disease'
        else:
            result = 'Low Risk of Heart Disease'

=======
    if model is None:
        return "Model not loaded. Please check server logs."

    try:
        # Collect features from form
        features = [float(x) for x in request.form.values()]
        # Pad with zeros if less than 13 features
        while len(features) < 13:
            features.append(0.0)

        final_features = np.array([features])
        prediction = model.predict(final_features)

        result = 'High Risk of Heart Disease' if prediction[0] == 1 else 'Low Risk of Heart Disease'
>>>>>>> d3b765688500478c8fd09abf46b83e973ba3ad35
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error occurred: {e}"

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(debug=True)
=======
# Run app locally or on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Only run Flask debug server if not on Render
    if os.environ.get("RENDER") is None:
        app.run(host="0.0.0.0", port=port, debug=True)
>>>>>>> d3b765688500478c8fd09abf46b83e973ba3ad35
