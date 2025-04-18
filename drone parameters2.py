import matplotlib.pyplot as plt
import random

# ---------------------- FRONTEND: SIMULATION + PLOT ----------------------

# Lists to store parameter data over 5 iterations
weights = []             # in kg
propeller_sizes = []     # in inches
battery_capacities = []  # in mAh

print("\n🔄 FRONTEND: Simulating Drone Parameter Configurations...\n")

# Simulate drone parameter values for 5 configurations
for i in range(5):
    print(f"🛠️ Iteration {i+1}: Simulating Parameters...")

    weight = round(random.uniform(1.5, 3.5), 2)             # Random weight in kg
    prop_size = random.choice([10, 12, 13, 14, 15])         # Inches
    battery = random.choice([5000, 8000, 10000, 12000])     # mAh

    weights.append(weight)
    propeller_sizes.append(prop_size)
    battery_capacities.append(battery)

    print(f"   Weight: {weight} kg")
    print(f"   Propeller Size: {prop_size} inches")
    print(f"   Battery Capacity: {battery} mAh\n")

# Plotting Weight vs Propeller Size
plt.figure(figsize=(10, 5))
plt.plot(propeller_sizes, weights, marker='o', linestyle='-', color='purple')
plt.title("Drone Weight vs. Propeller Size")
plt.xlabel("Propeller Size (inches)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

# ---------------------- BACKEND: HARDWARE CHECKS ----------------------

print("\n🔧 BACKEND: Validating Drone Parameters for Hardware Limits...\n")

# Define safe parameter limits
MAX_SAFE_WEIGHT = 3.2         # kg
MIN_PROPELLER_SIZE = 12       # inches
MIN_BATTERY_CAPACITY = 8000   # mAh

# Check each config and validate
for i in range(5):
    print(f"🧪 Iteration {i+1}: Validating Configuration...")

    weight = weights[i]
    prop_size = propeller_sizes[i]
    battery = battery_capacities[i]

    status = "✅ PASS"
    if weight > MAX_SAFE_WEIGHT:
        status = "❌ FAIL (Overweight)"
    elif prop_size < MIN_PROPELLER_SIZE:
        status = "❌ FAIL (Small Propeller)"
    elif battery < MIN_BATTERY_CAPACITY:
        status = "❌ FAIL (Low Battery Capacity)"

    print(f"   Weight: {weight} kg | Propeller: {prop_size}\" | Battery: {battery} mAh => {status}\n")
