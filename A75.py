# A75.py – Algorithm 75: Payload Drop Execution

import matplotlib.pyplot as plt
import time
import random

# ------------------------------
# Frontend: Simulation + Plot
# ------------------------------

# Step 1: Visualize the drone's position, target, and drop action
def plot_drop_execution(drone_position, drop_position, target_coords):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Define the target and positions
    target = target_coords  # Target is at the origin (0, 0)
    drone = drone_position
    payload = drop_position

    # Plot target (drop zone center)
    ax.plot(target[0], target[1], 'ro', label="Target Center", markersize=8)

    # Plot drone position (currently hovering before drop)
    ax.plot(drone[0], drone[1], 'bo', label="Drone Position", markersize=8)

    # Plot drop zone (circle)
    circle = plt.Circle((0, 0), 2.5, color='lightblue', alpha=0.6, label='Drop Zone')
    ax.add_patch(circle)

    # Plot payload drop location
    ax.plot(payload[0], payload[1], 'go', label="Payload Drop")

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Payload Drop Execution")
    ax.set_xlabel("X-axis (m)")
    ax.set_ylabel("Y-axis (m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Step 2: Simulate payload drop with position checking
def execute_payload_drop(drone_position, target_coords, acceptable_radius):
    print("Checking if drone is aligned for drop...")

    # Check if the drone is in range of the target (within acceptable radius)
    distance_to_target = ((drone_position[0] - target_coords[0])**2 + (drone_position[1] - target_coords[1])**2)**0.5
    if distance_to_target <= acceptable_radius:
        print("✅ Drone is in position for payload drop.")

        # Simulate the drop
        drop_x = random.uniform(target_coords[0] - acceptable_radius, target_coords[0] + acceptable_radius)
        drop_y = random.uniform(target_coords[1] - acceptable_radius, target_coords[1] + acceptable_radius)
        drop_position = (drop_x, drop_y)

        # Plot the drop execution
        plot_drop_execution(drone_position, drop_position, target_coords)

        print(f"\n--- Backend: Payload Drop Executed ---")
        print(f"Drop Coordinates: {drop_position}")
        print("✅ Payload successfully dropped!\n")
        return drop_position
    else:
        print("❌ Drone is not in position. Please adjust position and try again.")
        return None

# ------------------------------
# Backend: Drop Execution Logic
# ------------------------------

# Set target coordinates (assuming center at (0,0) for simplicity)
target_coords = (0, 0)
acceptable_radius = 2.5  # Drop tolerance in meters
drone_position = (0.5, 0.5)  # Drone's current position before the drop

# Execute the drop function
drop_position = execute_payload_drop(drone_position, target_coords, acceptable_radius)
