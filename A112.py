import matplotlib.pyplot as plt

# ------------ DRONE CLASS (updated) ------------ #
class Drone:
    def __init__(self, drone_id, mass_kg, battery_percent, payload_kg,
                 max_altitude_m, thrust_limit_N, gps_active=True, comm_link="Active"):

        self.drone_id = drone_id
        self.mass_kg = mass_kg
        self.battery_percent = battery_percent
        self.payload_kg = payload_kg
        self.max_altitude_m = max_altitude_m
        self.thrust_limit_N = thrust_limit_N

        self.initial_velocity_mps = 0
        self.position = {'x': 0, 'y': 0, 'z': 0}

        self.gps_active = gps_active
        self.comm_link = comm_link

        self.status_led = "BLINKING"
        self.initialized = False
        self.path = []  # to store movement

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
        self.path.append((x, y, z))  # Save for plotting

        # Backend simulation
        print("🛠️ Updating GPS coordinates...")
        print(f"🛰️ New position set to: X={x}, Y={y}, Z={z}")
        print("✔️ Motor adjustment successful.\n")

# ------------ MAIN EXECUTION ------------ #
if __name__ == "__main__":
    # Create drone
    drone1 = Drone(
        drone_id="MEDI-FLY-1",
        mass_kg=2.1,
        battery_percent=85,
        payload_kg=2.0,
        max_altitude_m=120,
        thrust_limit_N=18
    )

    drone1.show_status()
    drone1.backend_hardware_check()

    # Perform 5 navigations
    coordinates = [(10, 20, 5), (20, 25, 10), (30, 30, 15), (40, 35, 20), (50, 40, 25)]
    for pos in coordinates:
        drone1.navigate_to(*pos)

    # PLOT all 5 positions
    x_vals = [p[0] for p in drone1.path]
    y_vals = [p[1] for p in drone1.path]
    z_vals = [p[2] for p in drone1.path]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_vals, y_vals, z_vals, marker='o', color='blue', label='Drone Path')
    ax.set_title("Drone Navigation Path (5 Iterations)")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z (Altitude)')
    ax.legend()
    plt.tight_layout()
    plt.show()
