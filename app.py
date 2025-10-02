from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        # If less than 13 features, pad with zeros
        while len(features) < 13:
            features.append(0.0)

        final_features = np.array([features])
        prediction = model.predict(final_features)

        result = 'High Risk of Heart Disease' if prediction[0] == 1 else 'Low Risk of Heart Disease'
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error occurred: {e}"

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns PORT
    app.run(host="0.0.0.0", port=port, debug=True)
