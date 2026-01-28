from flask import Flask, jsonify
import thermal_model

app = Flask(__name__)

@app.route("/calculate", methods=["GET"])
def calculate_thermal():
    """
    API endpoint to return thermal analysis results
    """
    response = {
        "input": {
            "ambient_temperature_C": thermal_model.T_ambient,
            "power_W": thermal_model.Q
        },
        "results": {
            "total_thermal_resistance_C_per_W": round(thermal_model.R_total, 4),
            "junction_temperature_C": round(thermal_model.T_junction, 2)
        }
    }
    return jsonify(response)

@app.route("/")
def home():
    return "Thermal API is running. Use /calculate"

if __name__ == "__main__":
    app.run(debug=True)
