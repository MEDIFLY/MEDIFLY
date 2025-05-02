import matplotlib.pyplot as plt

# 🚀 Algorithm 98: Initialization and Parameter Setup

# 🧠 Frontend: Define all mission-related parameters
def initialize_mission_parameters():
    params = {
        "takeoff_altitude": 5,
        "cruise_altitude": 20,
        "payload_drop_altitude": 15,
        "return_base_altitude": 5,
        "landing_altitude": 0,
        "stage_durations": {
            "Takeoff": 5,
            "Climb": 10,
            "Payload Drop": 5,
            "Return": 7,
            "Landing": 3
        }
    }
    return params

# ⚙️ Backend: Execute initialization and return structured data
def setup_and_display_parameters():
    parameters = initialize_mission_parameters()

    print("🛠️ Mission Parameters Initialized:\n")
    for key, value in parameters.items():
        if isinstance(value, dict):
            print(f"📌 {key}:")
            for k, v in value.items():
                print(f"   - {k}: {v} seconds")
        else:
            print(f"📌 {key}: {value} meters")
    
    return parameters

# 🟣 Run setup
mission_params = setup_and_display_parameters()

# 📊 Frontend Plot: Mission altitude profile bar chart
altitudes = [
    mission_params["takeoff_altitude"],
    mission_params["cruise_altitude"],
    mission_params["payload_drop_altitude"],
    mission_params["return_base_altitude"],
    mission_params["landing_altitude"]
]
labels = ["Takeoff", "Climb", "Payload Drop", "Return", "Landing"]

plt.figure(figsize=(10, 6))
plt.bar(labels, altitudes, color='skyblue', edgecolor='black')
plt.title("📊 Mission Altitude Plan")
plt.ylabel("Altitude (m)")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
