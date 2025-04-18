import time

def apply_time_delay(delay_seconds):
    print(f"⏳ Applying time delay of {delay_seconds} second(s)...")
    time.sleep(delay_seconds)
    print("✅ Time delay completed.\n")

# Simulating 5 iterations with time delay after each takeoff step
for iteration in range(5):
    print(f"🔁 Iteration {iteration + 1} - Takeoff Step in Progress...")
    
    # Simulate placeholder for takeoff control logic
    print("🚁 Drone ascending...")

    # Backend + Frontend delay
    apply_time_delay(1)  # 1-second delay (can be changed to match real drone frequency)
