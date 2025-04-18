import random
import time
import matplotlib.pyplot as plt

# 📦 Backend Logic: Function to simulate initial position readings
def get_initial_position(iteration):
    print(f"\n📍 Iteration {iteration + 1}: Capturing Initial Position...")

    x = round(random.uniform(0.0, 10.0), 2)   # meters
    y = round(random.uniform(0.0, 10.0), 2)   # meters
    z = round(random.uniform(0.0, 5.0), 2)    # meters (altitude from ground)

    print(f"🧭 Position -> X: {x} m, Y: {y} m, Z: {z} m")

    return x, y, z

# 🔁 Storage for plotting
x_positions = []
y_positions = []
z_positions = []

# 🔄 Perform 5 Iterations
print("\n🔁 Performing 5 iterations of initial position capture...")
for i in range(5):
    x, y, z = get_initial_position(i)
    x_positions.append(x)
    y_positions.append(y)
    z_positions.append(z)
    time.sleep(1)

# 📊 Frontend: Plotting x, y, z positions
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_positions, y_positions, z_positions, c='blue', marker='o')

ax.set_title("Drone Initial Position (x, y, z) over 5 Iterations")
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Altitude (m)')

plt.tight_layout()
plt.show()

