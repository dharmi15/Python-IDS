from flask import Flask, request, jsonify
import joblib
import json

app = Flask(__name__)

# Load the model
model = joblib.load('decision_tree_model_xai.pkl')  # Adjust the path if necessary

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the POST request
        data = request.get_json(force=True)
        
        # Extract the 'X' value from the provided data
        X_new = data['X']
        
        # Predict using the loaded model
        predictions = model.predict(X_new)
        
        # Based on the prediction, return a custom message
        if predictions[0] == 1:
            return jsonify({"message": "Warning! Intrusion detected."})
        else:
            return jsonify({"message": "Safe. No Intrution activity detected."})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
