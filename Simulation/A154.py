import time
import numpy as np
import matplotlib.pyplot as plt

# ---- Frontend: Simulation of Drone's Payload Drop Process ----

# Drone and Payload Parameters
initial_position = [0, 0, 100]  # [x, y, z] in meters
drop_altitude = 20  # Altitude at which the payload will be released
drop_position = [0, 0, drop_altitude]  # Drop position (x, y, z)

# Flight Control (Assuming stability and correct position for simplicity)
def check_stability(position):
    # Dummy stability check (e.g., position check or sensor data)
    if position[2] <= drop_altitude:  # If the drone is at or below the drop altitude
        return True
    return False

# Simulate Payload Drop Execution
def payload_drop_execution():
    # Step 1: Drone checks if it's at the correct altitude
    current_position = initial_position.copy()
    print(f"Starting position: {current_position}")
    
    # Step 2: Begin descent towards the drop point
    descent = np.linspace(initial_position[2], drop_altitude, num=100)  # Descent trajectory
    for z in descent:
        current_position[2] = z
        time.sleep(0.1)  # Simulate time delay per iteration
        print(f"Descending to altitude: {current_position[2]} meters")
        
    # Step 3: Once at the drop altitude, execute payload drop
    if check_stability(current_position):
        print("Payload is dropped successfully!")
        current_position[2] = drop_altitude  # Payload release confirmed at drop altitude
        return True
    else:
        print("Failed to drop payload. Stability check failed.")
        return False

# ---- Backend: Hardware Interface for Payload Drop Execution ----

def execute_payload_drop():
    # Hardware Logic Simulation for Payload Drop
    print("Initiating Payload Drop on Hardware...")
    result = payload_drop_execution()
    
    # Confirmation of Payload Drop
    if result:
        print("Payload Drop completed successfully.")
    else:
        print("Payload Drop failed due to instability.")

# ---- Plotting the Descent Path ----

def plot_descent_path():
    # Simulate the descent path of the drone before the drop
    descent_altitudes = np.linspace(initial_position[2], drop_altitude, num=100)
    plt.figure(figsize=(8, 6))
    plt.plot(np.arange(len(descent_altitudes)), descent_altitudes, label="Altitude", color='blue')
    plt.axhline(y=drop_altitude, color='red', linestyle='--', label="Payload Drop Altitude")
    plt.title("Drone Descent Path During Payload Drop")
    plt.xlabel("Time Steps")
    plt.ylabel("Altitude (meters)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ---- Execute Simulation with Plot ----

if __name__ == "__main__":
    # Run the backend and frontend parts for the payload drop
    execute_payload_drop()
    plot_descent_path()
