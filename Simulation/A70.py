# A70.py – Algorithm 70: Payload Delivery System for Drone

import matplotlib.pyplot as plt
import numpy as np
import time
import random
from sklearn.linear_model import LinearRegression

# ------------------------------
# Frontend Simulation + Visualization
# ------------------------------

# Step 1: Dummy training for AI model
print("\n--- Training AI Model for Drop Offset Prediction ---")
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([0.9, 1.8, 3.1, 3.9, 5.2])  # Simulate slight noise

model = LinearRegression()
model.fit(X_train, y_train)
print("✅ Model trained.")

# Step 2: Simulate 5 missions
target_points = np.linspace(10, 50, 5)
predicted_offsets = model.predict(target_points.reshape(-1, 1))
actual_drops = predicted_offsets + np.random.normal(0, 0.5, 5)  # simulate minor error

# Step 3: Plot target vs actual
plt.figure(figsize=(7, 5))
plt.plot(target_points, predicted_offsets, 'go--', label='Predicted Drop Points (AI)')
plt.plot(target_points, actual_drops, 'ro--', label='Actual Drop Points (Hardware)')
for i in range(5):
    plt.plot([target_points[i], target_points[i]], [predicted_offsets[i], actual_drops[i]], 'k--', alpha=0.5)

plt.xlabel("Target Position")
plt.ylabel("Drop Location")
plt.title("Payload Delivery System Simulation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------
# Backend Hardware Integration
# ------------------------------

# Step 4: Simulated Servo Class
class ServoDropper:
    def __init__(self):
        self.status = "LOCKED"

    def drop_payload(self):
        print("🔧 Servo: Releasing payload...")
        time.sleep(1)
        self.status = "UNLOCKED"
        print("💊 Payload Dropped Successfully.")
        return True

    def reset(self):
        print("🔄 Servo Reset to LOCKED.")
        self.status = "LOCKED"

servo = ServoDropper()

# Step 5: Execute Full Delivery Loop
print("\n--- Backend: Full Payload Delivery Loop ---")
for i in range(5):
    print(f"\n🔁 Mission {i+1} Start:")
    print(f"📍 Target = {target_points[i]:.2f}m")
    
    predicted = predicted_offsets[i]
    actual = actual_drops[i]
    error = abs(actual - predicted)

    print(f"🤖 Predicted Drop = {predicted:.2f}m")
    print(f"📦 Actual Drop = {actual:.2f}m")
    print(f"🎯 Drop Error = {error:.2f}m")

    if servo.drop_payload():
        print("✅ Drop confirmed.")
    else:
        print("❌ Drop failure.")
    
    servo.reset()
    time.sleep(0.5)
