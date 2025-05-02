# A74.py – Algorithm 74: Drop Payload Function

import matplotlib.pyplot as plt
import time
import random

# ------------------------------
# Frontend: Simulation + Plot
# ------------------------------

# Step 1: Visualize the payload drop action
def plot_payload_drop(drop_position):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Define the target and payload positions
    target = (0, 0)  # Target is at the origin (0, 0)
    payload = drop_position  # Drop position will be passed here

    # Plot target (drop zone center)
    ax.plot(target[0], target[1], 'ro', label="Target Center", markersize=8)
    
    # Plot drop zone (circle)
    circle = plt.Circle((0, 0), 2.5, color='lightblue', alpha=0.6, label='Drop Zone')
    ax.add_patch(circle)
    
    # Plot payload drop location
    ax.plot(payload[0], payload[1], 'go', label="Payload Drop")
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Simulated Payload Drop")
    ax.set_xlabel("X-axis (m)")
    ax.set_ylabel("Y-axis (m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Step 2: Simulate dropping the payload
def drop_payload(target_coords, acceptable_radius):
    # Randomly simulate the drop location within the acceptable radius
    drop_x = random.uniform(target_coords[0] - acceptable_radius, target_coords[0] + acceptable_radius)
    drop_y = random.uniform(target_coords[1] - acceptable_radius, target_coords[1] + acceptable_radius)

    # Create the drop position
    drop_position = (drop_x, drop_y)
    
    # Plot the drop
    plot_payload_drop(drop_position)
    
    print(f"\n--- Backend: Payload Dropped ---")
    print(f"Drop Coordinates: {drop_position}")
    print("✅ Payload successfully dropped!\n")
    return drop_position

# ------------------------------
# Backend: Drop Logic
# ------------------------------

# Set target coordinates (assuming center at (0,0) for simplicity)
target_coords = (0, 0)
acceptable_radius = 2.5  # Drop tolerance in meters

# Call the function
drop_position = drop_payload(target_coords, acceptable_radius)
