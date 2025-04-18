import matplotlib.pyplot as plt
import random
import time

# ---------- Frontend (Simulation + Plot) ----------

# Simulated GPS coordinates (lat, lon)
start_gps = (12.9300, 77.5800)  # Example starting point
target_gps = (12.9500, 77.6000)  # Destination

# Simulated navigation steps
navigation_path = [start_gps]
current_gps = list(start_gps)

print("\n🔁 Simulating GPS Navigation...\n")

for i in range(10):
    # Move drone step-by-step toward target
    if current_gps[0] < target_gps[0]:
        current_gps[0] += round(random.uniform(0.001, 0.003), 5)
    if current_gps[1] < target_gps[1]:
        current_gps[1] += round(random.uniform(0.001, 0.003), 5)

    current_gps[0] = min(current_gps[0], target_gps[0])
    current_gps[1] = min(current_gps[1], target_gps[1])

    navigation_path.append(tuple(current_gps))
    print(f"📍 Step {i+1}: Drone at (Lat: {current_gps[0]}, Lon: {current_gps[1]})")
    time.sleep(0.3)  # Simulate real-time movement

# Plot the path
lats = [point[0] for point in navigation_path]
lons = [point[1] for point in navigation_path]

plt.figure(figsize=(8, 6))
plt.plot(lons, lats, marker='o', linestyle='-', color='blue', label='Path')
plt.scatter(start_gps[1], start_gps[0], color='green', s=100, label='Start')
plt.scatter(target_gps[1], target_gps[0], color='red', s=100, label='Target')

plt.title("Algorithm 30: GPS-Based Navigation")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ---------- Backend (Hardware Navigation Logic) ----------

def navigate_to_target(current_lat, current_lon, target_lat, target_lon):
    print("\n📡 Executing Backend GPS Navigation Logic...")
    path = [(current_lat, current_lon)]
    for i in range(10):
        if current_lat < target_lat:
            current_lat += 0.002
        if current_lon < target_lon:
            current_lon += 0.002

        current_lat = min(current_lat, target_lat)
        current_lon = min(current_lon, target_lon)

        path.append((current_lat, current_lon))
        print(f"🔧 Backend Step {i+1}: Lat {round(current_lat, 5)}, Lon {round(current_lon, 5)}")
        time.sleep(0.2)
    return path

# Simulate backend logic execution
navigate_to_target(12.9300, 77.5800, 12.9500, 77.6000)
