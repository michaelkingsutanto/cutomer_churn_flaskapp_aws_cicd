from flask import Flask, request, render_template, jsonify
from input_processing import validate, format_model_inputs
from model import Model
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        model_inputs = format_model_inputs(form_input)
        model_inputs_df = pd.DataFrame([model_inputs])
        prediction = Model().predict(model_inputs_df)[0]

        # Generate message based on the prediction
        if prediction == 1:
            prediction_message = "The customer is more likely to churn."
        else:
            prediction_message = "The customer is not likely to churn."
        return render_template('index.html', prediction=prediction_message)

    return render_template('index.html')


# Method 2: Via POST API (one prediction at a time)
@app.route('/api/predict_one', methods=['POST'])
def predict_one():
    try:
        request_data = request.get_json()  # optional: print request_data as log
        errors = validate(request_data)
        if len(errors) > 0:
            return jsonify({'errors': errors}), 400

        model_inputs = format_model_inputs(request_data)
        model_inputs_df = pd.DataFrame([model_inputs])
        prediction = Model().predict(model_inputs_df)
        # Convert prediction to a list to ensure it is JSON serializable
        return jsonify({'prediction': prediction.tolist()[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Method 2: Via POST API (many predictions at a time)
@app.route('/api/predict', methods=['POST'])
def predict_many():
    try:
        request_data = request.get_json()

        predictions = []
        model = Model()
        for row in request_data:
            errors = validate(row)
            if len(errors) > 0:
                return jsonify({'record': row, 'errors': errors}), 400

            model_inputs = format_model_inputs(row)
            model_inputs_df = pd.DataFrame([model_inputs])
            prediction = model.predict(model_inputs_df)
            # Convert prediction to a list to ensure it is JSON serializable
            predictions.append(prediction.tolist()[0])

        return jsonify({'predictions': predictions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
