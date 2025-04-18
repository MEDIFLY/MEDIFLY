import random
import matplotlib.pyplot as plt
import time

# -----------------------------
# FRONTEND: Simulation + Plot
# -----------------------------

def simulate_battery_levels(iterations=5):
    battery_levels = []
    for i in range(iterations):
        level = round(random.uniform(20, 100), 2)  # Simulate battery level between 20% to 100%
        print(f"[Simulation] Battery Level at Iteration {i+1}: {level}%")
        battery_levels.append(level)
        time.sleep(1)
    return battery_levels

def plot_battery_levels(levels):
    plt.figure(figsize=(8, 5))
    plt.plot(levels, marker='o', linestyle='--', color='blue', label='Battery Level')
    plt.axhline(y=30, color='red', linestyle='-', label='Low Battery Threshold (30%)')
    plt.title('Battery Level Over Time')
    plt.xlabel('Iteration')
    plt.ylabel('Battery Level (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------
# BACKEND: Hardware Logic
# -----------------------------

def verify_battery_levels(levels):
    for i, level in enumerate(levels):
        if level < 30:
            print(f"[Backend] WARNING: Battery low at Iteration {i+1} ({level}%). Initiating Return-To-Base protocol.")
        else:
            print(f"[Backend] Battery sufficient at Iteration {i+1} ({level}%). Continuing mission.")

# -----------------------------
# MAIN EXECUTION
# -----------------------------

if __name__ == "__main__":
    print("🔋 Starting Battery Level Verification...\n")
    
    battery_data = simulate_battery_levels()
    plot_battery_levels(battery_data)
    verify_battery_levels(battery_data)

    print("\n✅ Battery Verification Completed.")
