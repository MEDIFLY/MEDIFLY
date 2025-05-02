# ========================================
# Algorithm 2: Drone Parameters – Medifly
# Author: Maheshwari
# ========================================

import random
import time
import matplotlib.pyplot as plt

# ========================================
# 🧠 FRONTEND – Simulation (5 Iterations)
# ========================================

print("🧠 FRONTEND: Drone Thrust Simulation - 5 Iterations\n")

for i in range(5):
    print(f"--- Iteration {i+1} ---")

    # Define physical parameters
    drone_weight_kg = 2.5  # kg
    battery_capacity_mah = 22000  # mAh
    battery_voltage = 22.2  # Volts
    motor_thrust_per_motor_kg = 3.5
    number_of_motors = 4

    # Calculate thrust
    total_thrust_kg = motor_thrust_per_motor_kg * number_of_motors

    print(f"Total Drone Weight: {drone_weight_kg} kg")
    print(f"Total Thrust Capacity: {total_thrust_kg} kg")

    # Evaluation
    if total_thrust_kg > drone_weight_kg * 2:
        print("✅ Thrust is sufficient for stable flight and payload.\n")
    elif total_thrust_kg > drone_weight_kg:
        print("⚠️ Thrust is just enough, may struggle with payload.\n")
    else:
        print("❌ Thrust is not enough to lift the drone.\n")

    time.sleep(1)

# ========================================
# 🔌 BACKEND – Hardware Mock Integration
# ========================================

print("\n🔌 BACKEND: Real-time Hardware Simulation – 5 Iterations\n")

# Data storage for plotting
rpm_data = {"motor_1": [], "motor_2": [], "motor_3": [], "motor_4": []}
voltage_data = []
current_data = []

# Hardware simulation functions
def read_motor_data():
    return {
        "motor_1_rpm": random.randint(1200, 1300),
        "motor_2_rpm": random.randint(1200, 1300),
        "motor_3_rpm": random.randint(1200, 1300),
        "motor_4_rpm": random.randint(1200, 1300),
    }

def read_battery_data():
    return {
        "voltage": round(random.uniform(21.5, 22.2), 2),
        "current_draw": random.randint(15, 25)  # Amps
    }

# Run 5 iterations of hardware checks
for i in range(5):
    print(f"--- Iteration {i+1} ---")

    motor_data = read_motor_data()
    battery_data = read_battery_data()

    # Store values
    for m in range(1, 5):
        rpm_data[f"motor_{m}"].append(motor_data[f"motor_{m}_rpm"])
    voltage_data.append(battery_data["voltage"])
    current_data.append(battery_data["current_draw"])

    print(f"Motor RPMs: {motor_data}")
    print(f"Battery Voltage: {battery_data['voltage']}V")
    print(f"Battery Current Draw: {battery_data['current_draw']}A\n")
    time.sleep(1)

# ========================================
# 📈 PLOTTING RESULTS
# ========================================

# Plot 1: Motor RPMs
plt.figure(figsize=(10, 5))
for m in range(1, 5):
    plt.plot(rpm_data[f"motor_{m}"], marker='o', label=f"Motor {m} RPM")
plt.title("Motor RPMs over 5 Iterations")
plt.xlabel("Iteration")
plt.ylabel("RPM")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Battery Voltage & Current
plt.figure(figsize=(10, 5))
plt.plot(voltage_data, marker='o', color='blue', label="Voltage (V)")
plt.plot(current_data, marker='x', color='red', label="Current Draw (A)")
plt.title("Battery Stats over 5 iterations") 
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
