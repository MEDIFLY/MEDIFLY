# -*- coding: utf-8 -*-
# takeofffinbackend.py

print("Initializing MEDIFLY Backend System...\n")

# Simulated GPS response (In real case: read from serial port)
gps_data = {
    "latitude": 12.9716,
    "longitude": 77.5946,
    "status": "OK"
}

# Simulated battery voltage (in Volts)
battery_voltage = 22.5  # Example: 22.5V

# Simulated motor status
motor_status = "OK"

# -------------------------------------
# Performing System Check
# -------------------------------------
print("Performing System Check...\n")

# GPS Module Check
if gps_data["status"] == "OK":
    print(f"GPS Connected: Lat {gps_data['latitude']}, Lon {gps_data['longitude']}")
else:
    print("GPS Module Not Detected")

# Battery Status Check
if battery_voltage >= 22.2:
    print("Battery Status: OK")
else:
    print("Battery Voltage Low! Please Recharge.")

# Motor Check
if motor_status == "OK":
    print("Motor Check: OK")
else:
    print("Motor Failure Detected! Abort Mission.")

# -------------------------------------
# FINAL SYSTEM STATUS
# -------------------------------------
if gps_data["status"] == "OK" and battery_voltage >= 22.2 and motor_status == "OK":
    print("\nAll Systems Functional")
    print("MEDIFLY Drone Ready for Takeoff!")
else:
    print("\nSystem Check Failed. Please Resolve Issues Before Takeoff.")
