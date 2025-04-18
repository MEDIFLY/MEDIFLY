import matplotlib.pyplot as plt
import time

# ---------------------- Algorithm 91: Landing Parameters ----------------------
target_landing_altitude = 0.0
landing_tolerance = 0.1
descent_rate = 1.0
initial_altitude = 10.0

# ---------------------- Algorithm 92: Landing Function ----------------------
def perform_landing(current_altitude, descent_rate):
    altitudes = [current_altitude]
    while current_altitude > target_landing_altitude + landing_tolerance:
        current_altitude -= descent_rate
        current_altitude = max(current_altitude, target_landing_altitude)
        altitudes.append(current_altitude)
        print(f"Descending... Current Altitude: {current_altitude:.2f} m")
        time.sleep(0.2)
    return altitudes

# ---------------------- Algorithm 93: Execution of Landing ----------------------
def execute_landing():
    current_altitude = initial_altitude
    print(f"Initial Altitude: {current_altitude} m\n")
    altitude_log = perform_landing(current_altitude, descent_rate)

    # Plotting descent
    plt.plot(range(len(altitude_log)), altitude_log, marker='o', color='blue', linestyle='--')
    plt.title("Landing Altitude Descent")
    plt.xlabel("Time Step")
    plt.ylabel("Altitude (m)")
    plt.grid(True)
    plt.show()

    return altitude_log[-1]

# ---------------------- Algorithm 94: Simulation Execution ----------------------
def run_simulation_execution():
    print("🚀 Starting Drone Simulation...")
    
    # Initial state
    current_altitude = 10.0
    print(f"📍 Current Altitude: {current_altitude} m\n")
    
    # Begin landing procedure
    print("🛬 Executing Landing Phase...\n")
    final_altitude = execute_landing()

    # Final output
    if abs(final_altitude - target_landing_altitude) <= landing_tolerance:
        print("\n✅ Simulation Result: Drone Landed Successfully.")
    else:
        print("\n⚠️ Simulation Result: Landing Incomplete or Needs Manual Override.")

# ---------------------- Run the Simulation ----------------------
run_simulation_execution()
