import matplotlib.pyplot as plt
import random
import time

# ------------------ Backend Code (Hardware Logic Simulation) ------------------
class Drone:
    def __init__(self, drone_id):
        self.drone_id = drone_id
        self.mass = 2.1  # kg
        self.payload = 2.0  # kg
        self.battery = 85  # %
        self.max_altitude = 120  # meters
        self.thrust_limit = 18  # Newtons
        self.gps_active = True
        self.comm_link = True
        self.initialized = False
        self.position = {'x': 0, 'y': 0, 'z': 0}
        self.velocity = 0  # m/s
        self.status_led = "BLINKING"
        self.payload_dropped = False
        self.path = []  # Store all positions for plotting

    def initialize(self):
        if self.gps_active and self.comm_link and self.battery > 20:
            self.initialized = True
            self.status_led = "SOLID"
            print("\n🔧 Backend Check:")
            print("✅ GPS Module: LOCKED")
            print("✅ Communication Link: ESTABLISHED")
            print("🔋 Battery Status: OK")
            print("🟢 Drone Initialization: COMPLETE")
        else:
            print("❌ Initialization Failed: Check GPS/Comm/Battery")

    def navigate(self, x, y, z):
        if not self.initialized:
            print("🚫 Cannot Navigate: Drone not initialized.")
            return

        print(f"\n📍 Navigating to new position: ({x}, {y}, {z})")
        self.position['x'] = x + random.uniform(-1, 1)
        self.position['y'] = y + random.uniform(-1, 1)
        self.position['z'] = z + random.uniform(-0.5, 0.5)
        self.path.append((self.position['x'], self.position['y'], self.position['z']))
        print("🛠️ Updating GPS coordinates...")
        print(f"🛰️ New position set to: X={self.position['x']:.2f}, Y={self.position['y']:.2f}, Z={self.position['z']:.2f}")
        print("✔️ Motor adjustment successful.")

    def drop_payload(self):
        if self.payload > 0:
            print("\n📦 Initiating Payload Drop...")
            self.payload_dropped = True
            self.payload = 0
            print("✅ Payload successfully dropped.")
            print("🔧 Servo mechanism activated.")

    def show_status(self):
        print(f"\n🛩️ Drone ID: {self.drone_id}")
        print("─" * 30 + " Drone Parameters " + "─" * 30)
        print(f"Mass: {self.mass} kg")
        print(f"Battery: {self.battery}%")
        print(f"Payload: {self.payload} kg")
        print(f"Max Altitude: {self.max_altitude} m")
        print(f"Thrust Limit: {self.thrust_limit} N")
        print(f"GPS Active: {self.gps_active}")
        print(f"Comm Link: {self.comm_link}")
        print(f"Initial Velocity: {self.velocity} m/s")
        print(f"Position: {self.position}")
        print(f"Status LED: {self.status_led}")
        print(f"Initialized: {self.initialized}")
        print(f"Payload Dropped: {self.payload_dropped}")
        print("-─" * 40 + "\n")


# ------------------ Frontend (Simulation + Plots) ------------------
all_paths = []

for iteration in range(1, 6):
    print(f"\n\n===== ITERATION {iteration} START =====")
    drone = Drone("MEDI-FLY-1")
    drone.initialize()
    drone.show_status()

    waypoints = [
        (10, 20, 5),
        (20, 25, 10),
        (30, 30, 15),
        (40, 35, 20),
        (50, 40, 25),
    ]

    for idx, wp in enumerate(waypoints):
        drone.navigate(*wp)
        time.sleep(0.5)  # simulate delay
        if idx == 2:
            drone.drop_payload()

    all_paths.append(drone.path)
    print(f"===== ITERATION {iteration} END =====")

# -------------- Plotting all 5 runs in 3D --------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
colors = ['blue', 'green', 'red', 'purple', 'orange']

for i, path in enumerate(all_paths):
    x_vals = [p[0] for p in path]
    y_vals = [p[1] for p in path]
    z_vals = [p[2] for p in path]
    ax.plot(x_vals, y_vals, z_vals, label=f"Run {i+1}", color=colors[i])

ax.set_title("MEDIFLY Drone Path - 5 Iterations")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")
ax.set_zlabel("Altitude (Z)")
ax.legend()
plt.tight_layout()
plt.show()
