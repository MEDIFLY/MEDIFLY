import matplotlib.pyplot as plt

# 🚀 Algorithm 96: Parameters and Constants for Complete Mission

# 🧠 Frontend: Define mission parameters for simulation
MISSION_PARAMS = {
    "takeoff_altitude": 5,         # meters
    "cruise_altitude": 20,         # meters
    "payload_drop_altitude": 15,   # meters
    "max_speed": 10,               # m/s
    "min_speed": 2,                # m/s
    "battery_capacity": 100,       # percent
    "battery_usage_per_km": 5,     # percent/km
    "max_mission_duration": 600,   # seconds
    "total_distance": 10           # km
}

# ⚙️ Backend: Logic to compute estimated battery usage
def estimate_battery_usage(params):
    total_usage = params["total_distance"] * params["battery_usage_per_km"]
    remaining = params["battery_capacity"] - total_usage
    return total_usage, max(remaining, 0)

# Call backend function
battery_used, battery_remaining = estimate_battery_usage(MISSION_PARAMS)

# 🔍 Display Parameters
print("📦 Mission Constants and Parameters:")
for key, value in MISSION_PARAMS.items():
    print(f"  🔹 {key.replace('_', ' ').title()}: {value}")

print(f"\n🔋 Estimated Battery Used: {battery_used}%")
print(f"🔋 Estimated Battery Remaining: {battery_remaining}%")

# 📊 Frontend Visualization: Altitude profile vs Battery Usage
altitudes = [
    MISSION_PARAMS["takeoff_altitude"],
    MISSION_PARAMS["cruise_altitude"],
    MISSION_PARAMS["payload_drop_altitude"],
    0
]
battery_levels = [
    MISSION_PARAMS["battery_capacity"],
    battery_remaining + 10,  # assumed cruise drains 10%
    battery_remaining,       # drop drains more
    battery_remaining - 10   # assumed return uses more
]

plt.figure(figsize=(8, 5))
plt.plot(altitudes, battery_levels, marker='o', color='purple')
plt.title("🔋 Battery Usage vs Altitude")
plt.xlabel("Altitude (m)")
plt.ylabel("Battery Level (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
