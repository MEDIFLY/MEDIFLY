# AI Model 8: AI-Based Environmental Adaptation and Weather Prediction

import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.tree import DecisionTreeClassifier

# FRONTEND: Simulate environmental sensor readings
n_samples = 30
temperature = np.random.uniform(15, 40, n_samples)
humidity = np.random.uniform(20, 90, n_samples)
wind_speed = np.random.uniform(0, 25, n_samples)

# Label weather: 0=Clear, 1=Windy, 2=Rainy
weather_labels = []
for t, h, w in zip(temperature, humidity, wind_speed):
    if w > 15:
        weather_labels.append(1)  # Windy
    elif h > 70 and t < 25:
        weather_labels.append(2)  # Rainy
    else:
        weather_labels.append(0)  # Clear

X = np.column_stack((temperature, humidity, wind_speed))
y = np.array(weather_labels)

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Predict on new readings
new_reading = np.array([[28, 65, 5]])  # test data
predicted_weather = clf.predict(new_reading)[0]

weather_map = {0: "Clear", 1: "Windy", 2: "Rainy"}
print(f"Predicted Weather: {weather_map[predicted_weather]}")

# Backend: Adapt UAV parameters
def adjust_flight(weather_condition):
    if weather_condition == 0:
        return {"speed": "Normal", "angle": "0°"}
    elif weather_condition == 1:
        return {"speed": "Reduced", "angle": "5° tilt"}
    else:
        return {"speed": "Minimal", "angle": "10° downward"}

uav_response = adjust_flight(predicted_weather)
print(f"UAV Response → Speed: {uav_response['speed']}, Angle: {uav_response['angle']}")

# Plot 1: Environment Data and Weather Label
plt.figure(figsize=(6, 4))
colors = ['green' if label == 0 else 'orange' if label == 1 else 'blue' for label in y]
plt.scatter(wind_speed, humidity, c=colors)
plt.title("Weather Classification (Colors: Clear-Green, Windy-Orange, Rainy-Blue)")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Environmental Parameter Trend
plt.figure(figsize=(6, 4))
plt.plot(temperature, label='Temperature (°C)', color='red')
plt.plot(humidity, label='Humidity (%)', color='blue')
plt.plot(wind_speed, label='Wind Speed (km/h)', color='green')
plt.title("Environmental Parameters Over Time")
plt.xlabel("Sample Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
