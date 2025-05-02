# A78.py – Algorithm 78: Enhanced Drone Drop Simulation with Forces and Obstacle Detection

import time
import random
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# Frontend: Visualization + Plot
# ------------------------------

# Function to visualize the drone drop simulation
def plot_drone_drop_with_forces(drone_position, obstacle_positions, drop_zone):
    # Extract coordinates
    drone_x, drone_y = drone_position
    obstacle_x, obstacle_y = zip(*obstacle_positions)

    # Plot drone position, obstacles, and drop zone
    plt.figure(figsize=(8, 8))
    plt.plot(drone_x, drone_y, 'go', label="Drone", markersize=8)
    plt.scatter(obstacle_x, obstacle_y, color='red', label="Obstacles")
    plt.scatter(drop_zone[0], drop_zone[1], color='purple', label="Drop Zone", s=100)

    # Labels and legend
    plt.title("Enhanced Drone Drop Simulation with Forces and Obstacle Detection")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------------
# Backend: Drone Physics + Obstacle Avoidance
# ------------------------------

# Function to simulate external forces like wind and gravity
def simulate_forces(drone_position):
    # Simulate random wind force (affects X and Y direction)
    wind_force = random.uniform(-1, 1)
    # Simulate gravity effect on drone (affects Y direction)
    gravity_force = -9.81  # Simple gravity effect (constant for simulation)

    # Update drone position based on forces
    new_x = drone_position[0] + wind_force
    new_y = drone_position[1] + gravity_force  # Only gravity affects Y in this simulation

    return (new_x, new_y)

# Function to simulate obstacle detection and avoidance
def detect_and_avoid_obstacles(drone_position, obstacle_positions):
    for obstacle in obstacle_positions:
        # Calculate distance from drone to each obstacle
        distance = np.sqrt((drone_position[0] - obstacle[0]) ** 2 + (drone_position[1] - obstacle[1]) ** 2)
        # If the drone is too close to an obstacle (e.g., within 2 meters), simulate an avoidance maneuver
        if distance < 2.0:
            print("⚠️ Obstacle detected! Initiating avoidance maneuver.")
            # Move the drone away from the obstacle
            avoid_direction = np.array([drone_position[0] - obstacle[0], drone_position[1] - obstacle[1]])
            avoid_direction /= np.linalg.norm(avoid_direction)  # Normalize the direction
            drone_position = (drone_position[0] + avoid_direction[0], drone_position[1] + avoid_direction[1])
    return drone_position

# Function to simulate the drop execution while considering forces and obstacles
def drone_drop_with_forces_and_obstacles(initial_position, obstacle_positions, drop_zone):
    print("Starting Enhanced Drone Drop Simulation...")
    drone_position = initial_position

    # Simulate the drone path with forces and obstacles
    for i in range(10):  # Simulating 10 steps of movement
        # Simulate forces on the drone
        drone_position = simulate_forces(drone_position)
        # Detect and avoid obstacles
        drone_position = detect_and_avoid_obstacles(drone_position, obstacle_positions)

        print(f"Step {i + 1}: Drone Position: {drone_position}")
        
        # Plot the current state
        plot_drone_drop_with_forces(drone_position, obstacle_positions, drop_zone)
        
        # Simulate a short delay before the next move
        time.sleep(0.5)

    print("✅ Enhanced Drone Drop Simulation completed successfully.")

# ------------------------------
# Initialization
# ------------------------------

# Initial drone position (starting point)
initial_position = (0, 0)

# Obstacles (randomly generated within a defined area)
obstacle_positions = [(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(5)]

# Drop zone (target point)
drop_zone = (3, -3)

# Run the enhanced drone drop simulation
drone_drop_with_forces_and_obstacles(initial_position, obstacle_positions, drop_zone)
