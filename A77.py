# A77.py – Algorithm 77: GPS Relay Function

import time
import random
import matplotlib.pyplot as plt

# ------------------------------
# Frontend: Visualization + Plot
# ------------------------------

# Function to visualize GPS relay path and coordinates
def plot_gps_relay(drone_positions, ground_station_coords):
    # Extract positions for plotting
    x_coords = [pos[0] for pos in drone_positions]
    y_coords = [pos[1] for pos in drone_positions]

    # Plot drone path and ground station
    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, label="Drone Path", color='blue', marker='o')
    plt.plot(ground_station_coords[0], ground_station_coords[1], 'ro', label="Ground Station", markersize=10)

    plt.title("GPS Coordinates Relay to Ground Station")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------------
# Backend: GPS Relay Logic
# ------------------------------

# Function to simulate GPS coordinates for the drone
def simulate_gps_coordinates():
    # Generate random coordinates within a defined range for the drone
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    return (x, y)

# GPS relay function to send the coordinates to the ground station
def gps_relay_function(ground_station_coords, interval_seconds=5, max_transmissions=10):
    print("Starting GPS relay function...")

    # List to store drone positions
    drone_positions = []
    
    for _ in range(max_transmissions):
        # Simulate the current GPS coordinates of the drone
        current_gps = simulate_gps_coordinates()
        drone_positions.append(current_gps)

        # Print the GPS coordinates being sent
        print(f"Sending GPS Coordinates: {current_gps}")

        # Wait before sending the next set of coordinates (simulation of real-time)
        time.sleep(interval_seconds)
    
    # After all transmissions, visualize the GPS data relay
    plot_gps_relay(drone_positions, ground_station_coords)
    
    print("✅ GPS Coordinates successfully relayed to the ground station.")

# ------------------------------
# Initialization
# ------------------------------

# Ground station coordinates (fixed location)
ground_station_coords = (0, 0)

# Run the GPS relay function
gps_relay_function(ground_station_coords)
