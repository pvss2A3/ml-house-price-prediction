from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        features = np.array(input_data[['Dimensions', 'Plot Area']]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"predicted_price": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
