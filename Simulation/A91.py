import matplotlib.pyplot as plt
import time

# ---------------------- Backend: Landing Parameters Setup ----------------------
target_landing_altitude = 0.0           # meters (ground level)
max_descent_speed = 1.0                 # meters per second
landing_tolerance = 0.2                 # meters (acceptable stop zone)

# For iteration visualization
iterations = 5
initial_altitude = 10.0  # Starting altitude for the descent
altitudes_over_iterations = []

print("---- Backend: Landing Parameters Initialized ----")
print(f"Target Landing Altitude   : {target_landing_altitude} m")
print(f"Maximum Descent Speed     : {max_descent_speed} m/s")
print(f"Landing Tolerance         : ±{landing_tolerance} m")
print("--------------------------------------------------\n")

# ---------------------- Frontend: Simulation & Visualization ----------------------
print("---- Frontend: Simulating Landing Parameter Effects ----\n")
current_altitude = initial_altitude

for i in range(iterations):
    print(f"--- Iteration {i+1} ---")
    
    # Simulate descent based on max descent speed
    descent = min(max_descent_speed, current_altitude - target_landing_altitude)
    current_altitude -= descent
    
    # Store altitude for plotting
    altitudes_over_iterations.append(current_altitude)
    
    print(f"Current Altitude       : {current_altitude:.2f} m")
    print(f"Descent Applied        : {descent:.2f} m")
    
    # Check landing condition
    if abs(current_altitude - target_landing_altitude) <= landing_tolerance:
        print("Drone is within landing tolerance. Prepare for touchdown!\n")
    else:
        print("Drone still descending...\n")
    
    time.sleep(1)  # Simulated delay

# ---------------------- Plotting Altitude Descent Over Iterations ----------------------
plt.figure(figsize=(8, 5))
plt.plot(range(1, iterations + 1), altitudes_over_iterations, marker='o', linestyle='-', color='teal')
plt.title("Drone Altitude During Landing (Algorithm 91)")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.ylim(bottom=0)
plt.axhline(y=landing_tolerance, color='red', linestyle='--', label='Landing Tolerance')
plt.legend()
plt.tight_layout()
plt.show()
