# ----------------------------------------------------
# Algorithm 61: Prediction Method for Drop Offset Calculation
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

    def calculate_drop_offset(self, drone_params):
        """Calculate the predicted drop offset."""
        wind_offset = drone_params["wind_speed"] * self.wind_weight
        altitude_offset = drone_params["altitude"] * self.altitude_weight
        velocity_offset = drone_params["velocity"] * self.velocity_weight
        drop_offset = wind_offset + altitude_offset + velocity_offset
        return drop_offset

# Instantiate the AI model
ai_model = AIModel(model_weights["wind_factor_weight"],
                   model_weights["altitude_factor_weight"],
                   model_weights["velocity_factor_weight"])

# Initialize the AI model
ai_model.initialize_model()

# Simulate drop offset calculation over 5 iterations
drop_offsets = []
for i in range(5):
    drop_offset = ai_model.calculate_drop_offset(drone_params)
    
    # Simulate slight random adjustments to drone parameters
    drone_params["altitude"] += np.random.uniform(-0.5, 0.5)
    drone_params["velocity"] += np.random.uniform(-1.0, 1.0)
    drone_params["wind_speed"] += np.random.uniform(-2.0, 2.0)
    
    drop_offsets.append(drop_offset)
    print(f"Iteration {i+1}: Drop Offset Prediction = {drop_offset:.2f} meters")

# 🎨 Plot the drop offset values over iterations
plt.figure(figsize=(10, 5))

# Plotting drop offsets
plt.plot(range(1, 6), drop_offsets, 'ro-', label="Predicted Drop Offset")
plt.title("Prediction of Drop Offset Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Drop Offset (meters)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Drop Offset Calculation:")

# Simulate backend drop offset calculation for hardware deployment
for i in range(5):
    # Calculate the drop offset using the initialized model
    drop_offset = ai_model.calculate_drop_offset(drone_params)
    
    # Simulate changes in drone parameters (to reflect real-time updates)
    drone_params["altitude"] += np.random.uniform(-0.5, 0.5)  # Altitude fluctuation
    drone_params["velocity"] += np.random.uniform(-1.0, 1.0)  # Velocity fluctuation
    drone_params["wind_speed"] += np.random.uniform(-2.0, 2.0)  # Wind speed fluctuation
    
    print(f"[BACKEND] Iteration {i+1}: Drop Offset Prediction={drop_offset:.2f} meters, Altitude={drone_params['altitude']:.2f}, Velocity={drone_params['velocity']:.2f}, Wind Speed={drone_params['wind_speed']:.2f}")

print("\n✅ Drop Offset Calculation Processed Successfully.")
