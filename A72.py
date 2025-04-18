# A72.py – Algorithm 72: Payload Parameters

import matplotlib.pyplot as plt
import time

# ------------------------------
# Frontend: Simulation + Plot
# ------------------------------

# Step 1: Define payload parameters
payload_params = {
    "weight": 1.5,       # in kg
    "dimensions": (0.3, 0.2, 0.1),  # Length x Width x Height in meters
    "type": "Medical Kit",
    "packaging_type": "Shock-absorbent",
    "max_safe_drop_speed": 2.0  # m/s
}

# Step 2: Plot payload dimensions (visual representation)
dimensions = payload_params["dimensions"]
labels = ['Length', 'Width', 'Height']
colors = ['salmon', 'lightgreen', 'lightskyblue']

plt.figure(figsize=(6, 4))
bars = plt.bar(labels, dimensions, color=colors)
plt.ylabel("Meters")
plt.title("Payload Dimensions")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.1, yval + 0.01, f"{yval:.2f}", fontsize=9)

plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ------------------------------
# Backend: Payload Setup Logic
# ------------------------------

def initialize_payload_parameters():
    print("\n--- Backend: Payload Parameters Initialization ---")
    for param, val in payload_params.items():
        print(f"{param}: {val}")
    print("✅ Payload parameters initialized.\n")
    return payload_params

# Call the function
payload = initialize_payload_parameters()
