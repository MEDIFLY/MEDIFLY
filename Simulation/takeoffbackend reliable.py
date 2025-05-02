import time

def simulate_gps_status():
    return {"status": "OK", "lat": 12.9716, "lon": 77.5946}

def simulate_battery_voltage():
    return 22.5  # Simulated voltage

def simulate_motor_status():
    return "OK"

print("\nInitializing MEDIFLY Backend System...\n")

# Run 5 iterations of checks
for i in range(5):
    print(f"\n🌀 Iteration {i+1} System Check:")

    # GPS Check
    print("🔍 Checking GPS Module...")
    gps_data = simulate_gps_status()
    if gps_data["status"] == "OK":
        print(f"✅ GPS Connected: Lat {gps_data['lat']}, Lon {gps_data['lon']}")
    else:
        print("❌ GPS Not Connected. Abort Mission.")
        break

    # Battery Check
    print("🔋 Checking Battery Status...")
    battery_voltage = simulate_battery_voltage()
    if battery_voltage >= 22.2:
        print(f"✅ Battery OK: Voltage = {battery_voltage}V")
    else:
        print(f"❌ Low Battery: Voltage = {battery_voltage}V. Abort Mission.")
        break

    # Motor Check
    print("🛠️ Checking Motor Status...")
    motor_status = simulate_motor_status()
    if motor_status == "OK":
        print("✅ Motor Check: OK")
    else:
        print("❌ Motor Failure Detected! Abort Mission.")
        break

    time.sleep(1)  # Wait for 1 second before the next iteration

# Final Status after all checks
if gps_data["status"] == "OK" and battery_voltage >= 22.2 and motor_status == "OK":
    print("\n✅ All Systems Functional")
    print("🚀 MEDIFLY Drone Ready for Takeoff!")
else:
    print("\n⚠️ System Check Failed. Please Resolve Issues Before Takeoff.")
