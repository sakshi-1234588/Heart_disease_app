from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
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

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)