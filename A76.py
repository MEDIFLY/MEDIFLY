# A76.py – Algorithm 76: GPS Coordinates Relay to Ground Station

import time
import random
import matplotlib.pyplot as plt  # <-- Import matplotlib

# ------------------------------
# Frontend: Visualization + Plot
# ------------------------------

# Function to visualize drone's movement
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
# Backend: GPS Coordinates Relay Logic
# ------------------------------

# Simulate GPS coordinates for the drone
def simulate_gps_coordinates():
    # Generate random coordinates for the drone
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    return (x, y)

# Relay GPS coordinates to the ground station
def relay_gps_to_ground_station(ground_station_coords, interval_seconds=5, max_transmissions=10):
    print("Starting GPS relay to ground station...")

    # Simulate drone movement and GPS relaying
    drone_positions = []
    for _ in range(max_transmissions):
        # Simulate drone's GPS coordinates
        current_gps = simulate_gps_coordinates()
        drone_positions.append(current_gps)

        # Print and relay the coordinates
        print(f"Sending GPS Coordinates: {current_gps}")
        # Here, you would send these coordinates to a real ground station system
        # For this simulation, we'll just print them

        # Wait before sending the next coordinates (simulating real-time)
        time.sleep(interval_seconds)

    # After simulation, visualize the GPS relay
    plot_gps_relay(drone_positions, ground_station_coords)

    print("✅ GPS Coordinates successfully relayed to the ground station.\n")

# ------------------------------
# Initialization
# ------------------------------

# Ground station coordinates (fixed)
ground_station_coords = (0, 0)

# Relay GPS data
relay_gps_to_ground_station(ground_station_coords)
