import time
import matplotlib.pyplot as plt

print("🔧 Executing Algorithm 109: Drone Class Implementation (with Visuals)...\n")

# ================================
# 📦 FRONTEND: Simulation Notice
# ================================
print("📁 Creating and Testing Drone Class with Visual Logging...\n")

# ================================
# 🧠 BACKEND: Drone Class Definition
# ================================

class Drone:
    def __init__(self, x=0, y=0, z=0, battery=100, payload=True):
        self.x = x
        self.y = y
        self.z = z
        self.battery = battery
        self.payload_attached = payload
        self.mode = "IDLE"
        self.altitude_log = []
        self.mode_log = []
        self.time_log = []
        self.time_counter = 0
        print("🚁 Drone object created.")

    def log_state(self):
        self.altitude_log.append(self.z)
        self.mode_log.append(self.mode)
        self.time_log.append(self.time_counter)
        self.time_counter += 1

    def takeoff(self, target_altitude):
        print(f"🔼 Taking off to {target_altitude}m...")
        while self.z < target_altitude:
            self.z += 1
            self.mode = "ASCENDING"
            self.log_state()
            print(f"  ✈️ Altitude: {self.z}m")
            time.sleep(0.1)
        self.mode = "HOVER"
        self.log_state()
        print("✅ Reached hover altitude.")

    def drop_payload(self):
        if self.payload_attached:
            print("📦 Dropping payload...")
            self.payload_attached = False
            self.mode = "DROPPING"
            self.log_state()
            time.sleep(1)
            print("✅ Payload dropped.")
        else:
            print("⚠️ No payload to drop.")

    def return_to_base(self):
        print("🔙 Returning to base...")
        self.x = 0
        self.y = 0
        self.mode = "RETURNING"
        self.log_state()
        print("✅ Returned to base.")

    def land(self):
        print("🛬 Landing initiated...")
        while self.z > 0:
            self.z -= 1
            self.mode = "DESCENDING"
            self.log_state()
            print(f"  ⬇️ Altitude: {self.z}m")
            time.sleep(0.1)
        self.mode = "LANDED"
        self.log_state()
        print("✅ Drone landed safely.")

    def status(self):
        print(f"📊 STATUS: Pos=({self.x}, {self.y}, {self.z}) | Battery={self.battery}% | Payload={'Yes' if self.payload_attached else 'No'} | Mode={self.mode}")

# ================================
# 🔁 Iterative Testing
# ================================

for i in range(1, 6):
    print(f"\n🔁 Iteration {i} of Drone Testing\n{'-'*30}")
    drone = Drone()
    drone.status()
    drone.takeoff(5)
    drone.status()
    drone.drop_payload()
    drone.return_to_base()
    drone.land()
    drone.status()

    # ================================
    # 📊 Plotting Drone Altitude Over Time
    # ================================
    plt.figure(figsize=(8, 4))
    plt.plot(drone.time_log, drone.altitude_log, color='blue', linewidth=2, marker='o')
    plt.title(f'📈 Drone Altitude vs Time (Iteration {i})')
    plt.xlabel('Time')
    plt.ylabel('Altitude (meters)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print("\n✅ Algorithm 109 (with Plots) Complete!\n")
