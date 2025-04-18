# ---------------- FRONTEND: Simulated Current Sensor Values ----------------

def print_sensor_readings_frontend(temp, humidity, wind_speed, aqi):
    print("\n📟 Printing Current Environmental Sensor Readings:")
    print(f"🌡️ Temperature     : {temp} °C")
    print(f"💧 Humidity        : {humidity} %")
    print(f"🍃 Wind Speed      : {wind_speed} km/h")
    print(f"🫁 Air Quality (AQI): {aqi}")


# ---------------- BACKEND: Placeholder Fetch ----------------

def fetch_sensor_readings_backend():
    print("\n🛠️ Backend Fetch of Latest Sensor Data...")
    return {
        "temperature": 28.4,
        "humidity": 61.2,
        "wind_speed": 5.7,
        "air_quality": 110
    }


# ---------------- RUN BOTH FRONTEND + BACKEND ----------------

# Simulate backend fetching values
latest_data = fetch_sensor_readings_backend()

# Send to frontend print
print_sensor_readings_frontend(
    latest_data["temperature"],
    latest_data["humidity"],
    latest_data["wind_speed"],
    latest_data["air_quality"]
)
