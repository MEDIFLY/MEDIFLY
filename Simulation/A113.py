import matplotlib.pyplot as plt

# ------------ DRONE CLASS ------------ #
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
        self.path = []  # 3D path tracking
        self.payload_history = []  # for plotting
        self.payload_dropped = False

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
        self.payload_history.append(self.payload_kg)  # save payload for plotting

        # Backend simulation
        print("🛠️ Updating GPS coordinates...")
        print(f"🛰️ New position set to: X={x}, Y={y}, Z={z}")
        print("✔️ Motor adjustment successful.\n")

    def drop_payload(self):
        if self.payload_kg > 0 and not self.payload_dropped:
            print("📦 Initiating Payload Drop...")
            self.payload_kg = 0  # payload dropped
            self.payload_dropped = True
            print("✅ Payload successfully dropped.")
            print("🔧 Servo mechanism activated.\n")
        else:
            print("⚠️ No payload to drop or already dropped!\n")
        self.payload_history.append(self.payload_kg)  # save updated status

# ------------ MAIN EXECUTION ------------ #
if __name__ == "__main__":
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

    coordinates = [(10, 20, 5), (20, 25, 10), (30, 30, 15), (40, 35, 20), (50, 40, 25)]

    for i, pos in enumerate(coordinates):
        drone1.navigate_to(*pos)
        if i == 2:  # Drop payload at the 3rd position (index 2)
            drone1.drop_payload()

    # PLOT DRONE PATH
    x_vals = [p[0] for p in drone1.path]
    y_vals = [p[1] for p in drone1.path]
    z_vals = [p[2] for p in drone1.path]

    fig = plt.figure(figsize=(10, 4))

    # 3D Path Plot
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot(x_vals, y_vals, z_vals, marker='o', color='blue', label='Drone Path')
    ax1.set_title("Drone Navigation Path")
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z (Altitude)')
    ax1.legend()

    # Payload Plot
    ax2 = fig.add_subplot(122)
    ax2.plot(range(len(drone1.payload_history)), drone1.payload_history, marker='s', color='green')
    ax2.set_title("Payload Status Over Iterations")
    ax2.set_xlabel("Step")
    ax2.set_ylabel("Payload (kg)")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()
