# ------------------------------
# Algorithm 110 - Initialization of Drone Parameters (Improved Plot)
# ------------------------------

import matplotlib.pyplot as plt
import time
import random

# Storage for plotting
battery_levels = []
payload_weights = []
drone_labels = []

# --------- FRONTEND (Simulation) ---------
def initialize_drone_params(iteration):
    return {
        "Drone_ID": f"MEDI-FLY-{iteration}",
        "Mass_kg": round(random.uniform(1.5, 2.5), 2),
        "Battery_Level_%": random.randint(50, 100),
        "Payload_kg": round(random.uniform(0.1, 0.8), 2),
        "Max_Altitude_m": 120,
        "Thrust_Limit_N": random.randint(12, 20),
        "Initial_Velocity_mps": 0,
        "GPS_Active": True,
        "Comm_Link": "Active",
        "Initial_Position": {"x": 0, "y": 0, "z": 0}
    }

def print_params(params):
    print(f"\n🛩️  Drone Initialization - {params['Drone_ID']}")
    print("────────────────────────────")
    for key, value in params.items():
        if isinstance(value, dict):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value}")
    print("────────────────────────────\n")

# --------- BACKEND (Hardware Simulation) ---------
def backend_checks(params):
    print("🧩 Backend Hardware Simulation")
    if params['GPS_Active']:
        print("✅ GPS Module: LOCKED")
    else:
        print("❌ GPS Module: NOT DETECTED")

    if params['Comm_Link'] == "Active":
        print("✅ Comm Link: ESTABLISHED")
    else:
        print("❌ Comm Link: FAILED")

    if params['Battery_Level_%'] < 20:
        print("⚠️  Battery: CRITICAL LOW")
    else:
        print("🔋 Battery: OK")
    print("🟢 LED: Blinking - Initialization Success\n")
    time.sleep(1)

# --------- MAIN LOOP FOR 5 ITERATIONS ---------
for i in range(1, 6):
    print(f"\n🚀 STARTING ITERATION {i}")
    drone = initialize_drone_params(i)
    print_params(drone)
    backend_checks(drone)

    # Store data for plotting
    drone_labels.append(drone['Drone_ID'])
    battery_levels.append(drone['Battery_Level_%'])
    payload_weights.append(drone['Payload_kg'])

    print("✅ Initialization Complete for this drone.\n")
    print("===========================================\n")
    time.sleep(1)

# --------- FINAL VISUALIZATION (Two Y-Axes) ---------
fig, ax1 = plt.subplots(figsize=(10, 5))

x = range(len(drone_labels))

# Primary y-axis: Battery %
ax1.bar(x, battery_levels, width=0.4, color='green', label='Battery (%)', align='center')
ax1.set_ylabel('Battery Level (%)', color='green')
ax1.set_ylim(0, 110)

# Secondary y-axis: Payload kg
ax2 = ax1.twinx()
ax2.plot(x, payload_weights, color='blue', marker='o', label='Payload (kg)', linewidth=2)
ax2.set_ylabel('Payload Weight (kg)', color='blue')
ax2.set_ylim(0, 1)  # Payload is in kg (typically < 1 kg)

# X-axis and titles
plt.xticks(x, drone_labels)
plt.title("Drone Initialization: Battery vs Payload")
fig.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()
