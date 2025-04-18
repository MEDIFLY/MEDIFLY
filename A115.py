import math
import matplotlib.pyplot as plt

# ------------ DRONE CLASS ------------ #
class Drone:
    def __init__(self, drone_id, mass_kg, battery_percent, payload_kg,
                 max_altitude_m, thrust_limit_N, gps_active=True, comm_link="Active"):
        
        # Drone parameters initialization
        self.drone_id = drone_id
        self.mass_kg = mass_kg
        self.battery_percent = battery_percent
        self.payload_kg = payload_kg
        self.max_altitude_m = max_altitude_m
        self.thrust_limit_N = thrust_limit_N
        
        # Initial velocity and position
        self.initial_velocity_mps = 0
        self.position = {'x': 0, 'y': 0, 'z': 0}
        
        # GPS and Communication link status
        self.gps_active = gps_active
        self.comm_link = comm_link
        
        # Drone status and path tracking
        self.status_led = "BLINKING"
        self.initialized = False
        self.path = []  # 3D path tracking
        self.payload_history = []  # for plotting payload status
        self.altitude_history = []  # track altitude changes
        
        # Initialize payload dropped status
        self.payload_dropped = False  # Payload has not been dropped yet

    def show_status(self):
        print(f"\n🛩️ Drone ID: {self.drone_id}")
        print("────────────── Drone Parameters ──────────────")
        print(f"Mass: {self.mass_kg} kg")
        print(f"Battery: {self.battery_percent}%")
        print(f"Payload: {self.payload_kg} kg")
        print(f"Max Altitude: {self.max_altitude_m} m")
        print(f"Thrust Limit: {self.thrust_limit_N} N")
        print(f"GPS Active: {self.gps_active}")
        print(f"Comm Link: {self.comm_link}")
        print(f"Initial Velocity: {self.initial_velocity_mps} m/s")
        print(f"Position: {self.position}")
        print(f"Status LED: {self.status_led}")
        print(f"Initialized: {self.initialized}")
        print(f"Payload Dropped: {self.payload_dropped}")
        print("──────────────────────────────────────────────\n")

    def backend_hardware_check(self):
        print("🔧 Backend Check:")
        if self.gps_active:
            print("✅ GPS Module: LOCKED")
        else:
            print("❌ GPS Module: FAILED")

        if self.comm_link == "Active":
            print("✅ Communication Link: ESTABLISHED")
        else:
            print("❌ Communication Link: DISCONNECTED")

        if self.battery_percent < 20:
            print("⚠️ Battery: CRITICAL LOW")
        else:
            print("🔋 Battery Status: OK")

        self.status_led = "ON"
        self.initialized = True
        print("🟢 Drone Initialization: COMPLETE\n")

    def navigate_to(self, x, y, z):
        print(f"📍 Navigating to new position: ({x}, {y}, {z})")
        self.position['x'] = x
        self.position['y'] = y
        self.position['z'] = z
        self.path.append((x, y, z))
        self.payload_history.append(self.payload_kg)  # Save payload for plotting

        # Update altitude
        self.altitude_history.append(self.position['z'])

        # Backend simulation
        print("🛠️ Updating GPS coordinates...")
        print(f"🛰️ New position set to: X={x}, Y={y}, Z={z}")
        print("✔️ Motor adjustment successful.\n")

    def drop_payload(self):
        if self.payload_kg > 0 and not self.payload_dropped:
            print("📦 Initiating Payload Drop...")
            self.payload_kg = 0  # Payload dropped
            self.payload_dropped = True
            print("✅ Payload successfully dropped.")
            print("🔧 Servo mechanism activated.\n")
        else:
            print("⚠️ No payload to drop or already dropped!\n")
        self.payload_history.append(self.payload_kg)  # Save updated status

    # ------------ DROP ZONE CALCULATION ------------ #
    def calculate_drop_zone(self, wind_speed, wind_direction, time_to_drop):
        """
        Calculate the drop zone based on wind speed, wind direction, and the time the payload takes to drop.

        Parameters:
        - wind_speed (m/s): The speed of the wind affecting the drop.
        - wind_direction (degrees): The direction of the wind (angle with respect to the x-axis).
        - time_to_drop (seconds): The time it takes for the payload to fall to the ground from the drone.

        Returns:
        - drop_position (tuple): The estimated (x, y) position of the drop zone.
        """
        # Wind's effect on the drop zone
        wind_x = wind_speed * time_to_drop * math.cos(math.radians(wind_direction))
        wind_y = wind_speed * time_to_drop * math.sin(math.radians(wind_direction))

        # Calculate the new drop position based on the wind and drone's current position
        drop_x = self.position['x'] + wind_x
        drop_y = self.position['y'] + wind_y

        print(f"Calculated Drop Zone: X = {drop_x:.2f}, Y = {drop_y:.2f}")
        return drop_x, drop_y

# ------------ MAIN EXECUTION ------------ #
if __name__ == "__main__":
    # Initialize the drone object with parameters
    drone1 = Drone(
        drone_id="MEDI-FLY-1",
        mass_kg=2.1,
        battery_percent=85,
        payload_kg=2.0,
        max_altitude_m=120,
        thrust_limit_N=18
    )

    # Show drone status
    drone1.show_status()

    # Perform backend hardware check
    drone1.backend_hardware_check()

    # Coordinates to navigate to (x, y, z)
    coordinates = [(10, 20, 5), (20, 25, 10), (30, 30, 15), (40, 35, 20), (50, 40, 25)]

    # Move the drone and drop payload at the 3rd position
    for i, pos in enumerate(coordinates):
        drone1.navigate_to(*pos)
        if i == 2:  # Drop payload at the 3rd position (index 2)
            drone1.drop_payload()

    # Now, calculate the drop zone after the payload is dropped
    wind_speed = 5  # Wind speed in m/s
    wind_direction = 90  # Wind direction in degrees (East)
    time_to_drop = 5  # Time for the payload to drop (in seconds)

    drop_zone = drone1.calculate_drop_zone(wind_speed, wind_direction, time_to_drop)

    # Plotting drone path and drop zone
    x_vals, y_vals = zip(*[(pos[0], pos[1]) for pos in drone1.path])  # Extract only X, Y coordinates for path plotting
    drop_x, drop_y = drop_zone  # Drop zone from the calculation

    # Plot the drone's path
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, marker='o', label="Drone Path", color='b', linestyle='-', markersize=8)
    
    # Plot the drop zone
    plt.scatter(drop_x, drop_y, color='r', label="Drop Zone", s=100, edgecolor='black')

    # Add labels and title
    plt.title('Drone Path and Calculated Drop Zone')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()
