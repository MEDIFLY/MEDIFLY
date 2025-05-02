import matplotlib.pyplot as plt
import time

# Algorithm 95: Drone Flight Simulation Overview

# Time stamps for each flight phase (in seconds)
time_log = [0, 5, 10, 15, 20, 25, 30, 35]

# Altitude at each phase (in meters)
altitude_profile = [0, 5, 5, 5, 5, 5, 0, 0]  # Fixed: 8 points to match time_log

def simulate_full_flight():
    print("🚁 Starting MEDIFLY Drone Flight Simulation Overview...\n")
    flight_phases = [
        "Takeoff",
        "Hovering",
        "Navigation to Target",
        "Obstacle Check",
        "Payload Drop",
        "Return to Base",
        "Landing"
    ]

    for i, phase in enumerate(flight_phases):
        print(f"⏱️ Phase: {phase} at time {time_log[i]}s")
        time.sleep(0.3)  # Optional short delay to simulate phase timing

    print("\n✅ Flight Simulation Completed.\n")

    # Plotting the altitude profile
    plt.figure(figsize=(10, 5))
    plt.plot(time_log, altitude_profile, marker='o', color='green', linestyle='-', linewidth=2)
    plt.title("📊 MEDIFLY Drone Altitude Profile Over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Altitude (meters)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run the simulation
simulate_full_flight()
