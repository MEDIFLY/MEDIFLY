import matplotlib.pyplot as plt
import time

# Initialize time step parameters
initial_time = 0
time_step = 1  # seconds
total_iterations = 5

# Logs for plotting
time_log = []
simulated_time = initial_time

print("⏱️ Starting Algorithm 105: Time Increment\n")

# ✅ FRONTEND: Simulation Time Increment Loop
for i in range(total_iterations):
    print(f"🔁 Iteration {i+1}")
    print(f"  ➤ Current Time: {simulated_time} seconds")
    time_log.append(simulated_time)
    simulated_time += time_step
    time.sleep(0.5)

# 📊 Plotting Time Increments
plt.figure(figsize=(8, 4))
plt.plot(range(1, total_iterations + 1), time_log, marker='o', linestyle='-', color='blue')
plt.title("⏱️ Simulation Time Progression (A105)")
plt.xlabel("Iteration")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ BACKEND: Hardware Timer Function
def increment_time(current_time, increment=1):
    return current_time + increment

# Example backend logic
print("\n🧠 Backend Time Increment Check:")
hardware_time = 0
for i in range(5):
    hardware_time = increment_time(hardware_time)
    print(f"  ➤ Hardware Time at Iteration {i+1}: {hardware_time} seconds")
