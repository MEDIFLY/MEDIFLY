# A120.py
import matplotlib.pyplot as plt
import time
import random

# ─────────────────────────────────────
# 🧪 Equipment State Definitions
# ─────────────────────────────────────
equipment_states = {
    "Oxygen Tank": "OK",
    "Defibrillator": "OK",
    "Cold Storage": "OK",
    "Syringe Box": "OK",
    "Glucose Pack": "OK"
}

# Store state history for plotting
time_series = []
oxygen_status = []
cold_storage_temp = []
battery_level = []

# ─────────────────────────────────────
# 🔧 Backend Monitoring Simulation
# ─────────────────────────────────────
print("🧰 Medical Equipment State Monitoring Started\n")

for t in range(0, 25, 5):  # Simulate every 5 seconds
    print(f"⏱️ Time = {t} sec")

    # Simulate state changes and sensor readings
    temp = random.uniform(2.0, 8.0)  # Cold storage temp (°C)
    batt = random.randint(70, 100)   # Battery %
    oxygen = "LOW" if random.random() < 0.1 else "OK"

    # Update state dictionary
    equipment_states["Oxygen Tank"] = oxygen
    equipment_states["Cold Storage"] = "OK" if 2.0 <= temp <= 8.0 else "ALERT"

    # Append to series for plotting
    time_series.append(t)
    oxygen_status.append(0 if oxygen == "LOW" else 1)
    cold_storage_temp.append(temp)
    battery_level.append(batt)

    # Print status
    for eq, state in equipment_states.items():
        status_icon = "✅" if state == "OK" else "⚠️"
        print(f"   {status_icon} {eq}: {state}")
    
    print(f"   🌡️ Cold Storage Temp: {temp:.2f}°C")
    print(f"   🔋 Battery Level: {batt}%\n")
    time.sleep(0.3)

# ─────────────────────────────────────
# 📊 FRONTEND PLOTS
# ─────────────────────────────────────
plt.figure(figsize=(12, 6))

# Oxygen Status
plt.subplot(1, 3, 1)
plt.plot(time_series, oxygen_status, marker='o', color='green')
plt.ylim(-0.2, 1.2)
plt.yticks([0, 1], labels=["LOW", "OK"])
plt.title("Oxygen Tank Status")
plt.xlabel("Time (s)")
plt.grid(True)

# Cold Storage Temperature
plt.subplot(1, 3, 2)
plt.plot(time_series, cold_storage_temp, marker='o', color='blue')
plt.axhline(2.0, color='red', linestyle='--')
plt.axhline(8.0, color='red', linestyle='--')
plt.title("Cold Storage Temperature (°C)")
plt.xlabel("Time (s)")
plt.ylabel("Temp (°C)")
plt.grid(True)

# Battery Level
plt.subplot(1, 3, 3)
plt.plot(time_series, battery_level, marker='o', color='orange')
plt.title("Battery Level (%)")
plt.xlabel("Time (s)")
plt.ylabel("Battery (%)")
plt.grid(True)

plt.tight_layout()
plt.suptitle("📦 MEDIFLY Medical Equipment State Monitoring", fontsize=14, y=1.05)
plt.show()
