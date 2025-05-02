import matplotlib.pyplot as plt
import time

# ---------------------- Landing Parameters ----------------------
target_landing_altitude = 0.0
max_descent_speed = 1.0
landing_tolerance = 0.2
initial_altitude = 10.0
altitudes = []

# ---------------------- Backend: Landing Function ----------------------
def perform_landing(current_altitude):
    print("\n🔧 Landing Function Activated")
    iteration = 1
    while abs(current_altitude - target_landing_altitude) > landing_tolerance and iteration <= 5:
        print(f"\n--- Iteration {iteration} ---")
        
        descent = min(max_descent_speed, current_altitude - target_landing_altitude)
        current_altitude -= descent
        altitudes.append(current_altitude)
        
        print(f"Current Altitude: {current_altitude:.2f} m")
        print(f"Descent Applied : {descent:.2f} m")
        
        if abs(current_altitude - target_landing_altitude) <= landing_tolerance:
            print("✅ Drone within landing tolerance. Ready to land.\n")
        else:
            print("⬇️ Drone still descending...")

        iteration += 1
        time.sleep(1)
    return current_altitude

# ---------------------- Algorithm 93: Execution of Landing ----------------------
def execute_landing():
    print("\n🚁 Initiating Drone Landing Sequence")
    final_altitude = perform_landing(initial_altitude)

    if abs(final_altitude - target_landing_altitude) <= landing_tolerance:
        print(f"\n✅ Landing Successful. Final Altitude: {final_altitude:.2f} m")
    else:
        print(f"\n⚠️ Landing Incomplete. Final Altitude: {final_altitude:.2f} m")

    return final_altitude

# ---------------------- Run the Landing Execution ----------------------
final_altitude = execute_landing()

# ---------------------- Plotting Descent ----------------------
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(altitudes) + 1), altitudes, marker='o', color='darkgreen', linestyle='-')
plt.axhline(y=landing_tolerance, color='red', linestyle='--', label='Landing Tolerance')
plt.title("Execution of Landing: Descent Curve")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.ylim(bottom=0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
