# A116.py – Drop Zone Visualization with Path + Plots
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Drone Class
class Drone:
    def __init__(self, drone_id):
        self.id = drone_id
        self.path = []
        self.position = {'x': 0, 'y': 0, 'z': 0}
        self.payload_dropped = False

    def navigate_to(self, x, y, z):
        self.position = {'x': x, 'y': y, 'z': z}
        self.path.append((x, y, z))
        print(f"📍 Navigating to ({x}, {y}, {z})")

    def drop_payload(self):
        if not self.payload_dropped:
            self.payload_dropped = True
            print("📦 Payload dropped.")
        else:
            print("⚠️ Payload already dropped!")

# Initialize drone
drone1 = Drone("MEDI-FLY-1")

# Simulate flight + drop
drone1.navigate_to(10, 20, 5)
drone1.navigate_to(20, 25, 10)
drone1.navigate_to(30, 30, 15)
drop_point = (30, 30, 15)
drone1.drop_payload()
drone1.navigate_to(40, 35, 20)
drone1.navigate_to(50, 40, 25)

# Estimated drop zone (based on simplistic wind drift model)
drop_zone = (drone1.position['x'], drone1.position['y'] + 25, 0)

# Plotting the path
x_vals = [p[0] for p in drone1.path]
y_vals = [p[1] for p in drone1.path]
z_vals = [p[2] for p in drone1.path]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Drone path
ax.plot(x_vals, y_vals, z_vals, label='Drone Path', color='blue', linewidth=2)

# Drop point
ax.scatter(*drop_point, color='red', s=100, label='Drop Point')
ax.text(*drop_point, 'Drop Point', color='red')

# Drop zone
ax.scatter(*drop_zone, color='green', s=100, label='Estimated Drop Zone')
ax.text(*drop_zone, 'Drop Zone', color='green')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (Altitude)')
ax.set_title('Payload Drop Zone Visualization')
ax.legend()
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.show()
