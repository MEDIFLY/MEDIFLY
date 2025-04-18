# ALGORITHM 1: SYSTEM CHECK (FRONTEND + BACKEND)

import random
import matplotlib.pyplot as plt
import time

# ===========================
# FRONTEND (SIMULATION + PLOTS)
# ===========================

print("\U0001F501 Performing 5 simulated frontend system checks...\n")

# Sample data stores
gps_data = []
battery_data = []
motor_data = []
iterations = list(range(5))

# Run simulation for 5 iterations
for i in iterations:
    print(f"\U0001F4F1 Iteration {i+1}: Checking Systems...")

    # Simulate GPS
    lat = round(random.uniform(12.90, 12.99), 4)
    lon = round(random.uniform(77.54, 77.68), 4)
    gps_data.append((lat, lon))
    print(f"\u2705 GPS: Lat {lat}, Lon {lon}")

    # Simulate Battery
    voltage = round(random.uniform(22.5, 24.5), 2)
    battery_data.append(voltage)
    print(f"\U0001F50B Battery: {voltage} V")

    # Simulate Motor Status
    motor_ok = random.choice([0, 1])  # 1 = OK, 0 = Not OK
    motor_data.append(motor_ok)
    status_text = "OK" if motor_ok else "Not OK"
    print(f"\u2699\ufe0f Motor Status: {status_text}\n")

# --- Plotting ---
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Battery Voltage Plot
axs[0].plot(iterations, battery_data, marker='o', color='blue', linestyle='-')
axs[0].set_title("Battery Voltage over Iterations")
axs[0].set_xlabel("Iteration")
axs[0].set_ylabel("Voltage (V)")
axs[0].grid(True)

# Motor Status Plot
axs[1].plot(iterations, motor_data, marker='x', color='green', linestyle='--')
axs[1].set_title("Motor Status over Iterations (1=OK, 0=Not OK)")
axs[1].set_xlabel("Iteration")
axs[1].set_ylabel("Status")
axs[1].set_yticks([0, 1])
axs[1].grid(True)

plt.tight_layout()
plt.show()

# ===========================
# BACKEND (HARDWARE LOGIC)
# ===========================

def check_hardware_system(iteration):
    print(f"\n\U0001F4BB [BACKEND] Hardware Check - Iteration {iteration+1}")

    # Simulated GPS read
    gps_lat = gps_data[iteration][0]
    gps_lon = gps_data[iteration][1]
    print(f"GPS Coordinates: ({gps_lat}, {gps_lon})")

    # Battery voltage logic
    voltage = battery_data[iteration]
    if voltage < 23.0:
        print(f"Battery LOW: {voltage}V - Please Recharge!")
    else:
        print(f"Battery OK: {voltage}V")

    # Motor status logic
    if motor_data[iteration] == 0:
        print("Motor Issue Detected - Please Inspect Motor")
    else:
        print("Motor Running Smoothly")

# Perform hardware-like backend checks
for i in iterations:
    check_hardware_system(i)
    time.sleep(1)  # Simulate hardware delay
