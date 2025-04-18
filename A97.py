import time
import matplotlib.pyplot as plt

# 🚀 Algorithm 97: Main Simulation Routine

# 🧠 Frontend: Define flight stages and corresponding altitudes and timestamps
flight_stages = [
    ("Takeoff", 5),
    ("Climb to Cruise Altitude", 20),
    ("Payload Drop", 15),
    ("Return to Base", 5),
    ("Landing", 0)
]

stage_durations = [5, 10, 5, 7, 3]  # seconds per stage

# ⚙️ Backend: Simulate each stage and collect data
altitude_log = []
time_log = []
stage_log = []

def simulate_main_mission():
    print("🚁 Starting Main MEDIFLY Mission Routine...\n")
    current_time = 0

    for i, (stage, altitude) in enumerate(flight_stages):
        print(f"⏱️ Time {current_time}s: ✈️ {stage} to {altitude}m")
        time_log.append(current_time)
        altitude_log.append(altitude)
        stage_log.append(stage)
        time.sleep(0.5)  # Simulate wait (for demo)
        current_time += stage_durations[i]

    print("\n✅ Mission Routine Completed.")

# 🟣 Run simulation
simulate_main_mission()

# 📊 Frontend Visualization
plt.figure(figsize=(10, 6))
plt.plot(time_log, altitude_log, marker='o', color='blue', linewidth=2)
for i, txt in enumerate(stage_log):
    plt.annotate(txt, (time_log[i], altitude_log[i] + 1), fontsize=9, rotation=15)

plt.title("📈 MEDIFLY: Main Mission Routine - Altitude vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.tight_layout()
plt.show()
