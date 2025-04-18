# ----------------------------------------------------
# Algorithm 60: Model Initialization with Defined Weights
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =======================
# FRONTEND: Simulation
# =======================

# Define model weights for initialization
model_weights = {
    "wind_factor_weight": 0.7,
    "altitude_factor_weight": 0.5,
    "velocity_factor_weight": 0.3,
}

# Simulate drone parameters for prediction
drone_params = {
    "altitude": 15.0,  # in meters
    "velocity": 8.0,  # in m/s
    "wind_speed": 4.0,  # in m/s
}

# Initialize AI model with predefined weights
class AIModel:
    def __init__(self, wind_weight, altitude_weight, velocity_weight):
        """Initialize the AI model with predefined weights."""
        self.wind_weight = wind_weight
        self.altitude_weight = altitude_weight
        self.velocity_weight = velocity_weight

    def initialize_model(self):
        """Simulate the initialization of the model with defined weights."""
        print("\n🔧 Initializing AI Model with Defined Weights:")
        print(f"Wind Weight: {self.wind_weight}")
        print(f"Altitude Weight: {self.altitude_weight}")
        print(f"Velocity Weight: {self.velocity_weight}")
        print("AI Model Initialized Successfully!")

    def calculate_prediction(self, drone_params):
        """Calculate the predicted value (drop offset) based on weights."""
        wind_offset = drone_params["wind_speed"] * self.wind_weight
        altitude_offset = drone_params["altitude"] * self.altitude_weight
        velocity_offset = drone_params["velocity"] * self.velocity_weight
        prediction = wind_offset + altitude_offset + velocity_offset
        return prediction

# Instantiate the AI model with predefined weights
ai_model = AIModel(model_weights["wind_factor_weight"],
                   model_weights["altitude_factor_weight"],
                   model_weights["velocity_factor_weight"])

# Initialize the AI model
ai_model.initialize_model()

# Simulate predictions over 5 iterations
predictions = []
for i in range(5):
    prediction = ai_model.calculate_prediction(drone_params)
    
    # Simulate slight random adjustments to drone parameters
    drone_params["altitude"] += np.random.uniform(-0.5, 0.5)
    drone_params["velocity"] += np.random.uniform(-1.0, 1.0)
    drone_params["wind_speed"] += np.random.uniform(-2.0, 2.0)
    
    predictions.append(prediction)
    print(f"Iteration {i+1}: Prediction = {prediction:.2f} meters")

# 🎨 Plot the prediction values over iterations
plt.figure(figsize=(10, 5))

# Plotting predictions
plt.plot(range(1, 6), predictions, 'bo-', label="Predicted Payload Drop Offset")
plt.title("AI Model Initialization and Prediction Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Predicted Payload Drop Offset (meters)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Model Initialization and Prediction Processing:")

# Simulate backend prediction and processing for hardware deployment
for i in range(5):
    # Calculate the predicted drop offset using the initialized model
    prediction = ai_model.calculate_prediction(drone_params)
    
    # Simulate changes in drone parameters (to reflect real-time updates)
    drone_params["altitude"] += np.random.uniform(-0.5, 0.5)  # Altitude fluctuation
    drone_params["velocity"] += np.random.uniform(-1.0, 1.0)  # Velocity fluctuation
    drone_params["wind_speed"] += np.random.uniform(-2.0, 2.0)  # Wind speed fluctuation
    
    print(f"[BACKEND] Iteration {i+1}: Prediction={prediction:.2f} meters, Altitude={drone_params['altitude']:.2f}, Velocity={drone_params['velocity']:.2f}, Wind Speed={drone_params['wind_speed']:.2f}")

print("\n✅ Model initialized and prediction processed successfully.")
