from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Lifespan Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400  # Bad request

        # Check if all required fields are present
        required_fields = [
            "gender", "age", "occupation", "sleep_duration", "quality_of_sleep",
            "physical_activity", "stress_level", "bmi_category", "blood_pressure",
            "heart_rate", "daily_steps", "sleep_disorder"
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Dummy Prediction (Replace with actual model)
        predicted_lifespan = 75.4  # Example fixed output

        response = {
            "Predicted Lifespan": predicted_lifespan
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
