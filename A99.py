import matplotlib.pyplot as plt

# 🔄 Algorithm 99: Main Simulation Loop

# 📌 Reuse the initialization from Algorithm 98
def initialize_mission_parameters():
    return {
        "takeoff_altitude": 5,
        "cruise_altitude": 20,
        "payload_drop_altitude": 15,
        "return_base_altitude": 5,
        "landing_altitude": 0,
        "stage_durations": {
            "Takeoff": 5,
            "Climb": 10,
            "Payload Drop": 5,
            "Return": 7,
            "Landing": 3
        }
    }

# 🔁 Backend: Simulate drone mission phases
def run_main_simulation_loop():
    print("🚁 Starting Main Mission Simulation Loop...\n")
    
    mission = initialize_mission_parameters()
    stages = mission["stage_durations"]
    
    time_log = []
    altitude_log = []
    
    current_time = 0
    
    # ⏫ Takeoff
    print(f"⏱️ {current_time}s - Takeoff Phase: Altitude {mission['takeoff_altitude']}m")
    time_log.append(current_time)
    altitude_log.append(mission["takeoff_altitude"])
    current_time += stages["Takeoff"]

    # ⛰️ Climb to Cruise
    print(f"⏱️ {current_time}s - Climb Phase: Altitude {mission['cruise_altitude']}m")
    time_log.append(current_time)
    altitude_log.append(mission["cruise_altitude"])
    current_time += stages["Climb"]

    # 🎯 Payload Drop
    print(f"⏱️ {current_time}s - Payload Drop Phase: Altitude {mission['payload_drop_altitude']}m")
    time_log.append(current_time)
    altitude_log.append(mission["payload_drop_altitude"])
    current_time += stages["Payload Drop"]

    # 🔁 Return to Base
    print(f"⏱️ {current_time}s - Return Phase: Altitude {mission['return_base_altitude']}m")
    time_log.append(current_time)
    altitude_log.append(mission["return_base_altitude"])
    current_time += stages["Return"]

    # 🛬 Landing
    print(f"⏱️ {current_time}s - Landing Phase: Altitude {mission['landing_altitude']}m")
    time_log.append(current_time)
    altitude_log.append(mission["landing_altitude"])
    current_time += stages["Landing"]

    print(f"\n✅ Mission Simulation Complete at {current_time}s.")
    
    return time_log, altitude_log

# 🎮 Run simulation
time_series, altitude_series = run_main_simulation_loop()

# 📊 Frontend Plot: Time vs Altitude
plt.figure(figsize=(10, 6))
plt.plot(time_series, altitude_series, marker='o', linestyle='-', color='green')
plt.title("📈 Drone Altitude Profile Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.tight_layout()
plt.show()
