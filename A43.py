import matplotlib.pyplot as plt
import time

# ----------------------------
# INITIAL SETUP
# ----------------------------
iterations = 5
ki_fixed = 0.1
ki_values = []

print("⚙️ Integral Gain (ki) Configuration\n")

# ----------------------------
# FRONTEND + BACKEND SIMULATION
# ----------------------------
for i in range(iterations):
    print(f"\n🔁 Iteration {i+1}:")
    current_ki = ki_fixed

    print(f"  🔸 ki value for this iteration: {current_ki}")

    # Backend: Simulate sending to hardware
    hardware_packet = {
        "parameter": "ki",
        "value": current_ki
    }

    print(f"  🛠️ Backend Sending → {hardware_packet}")

    ki_values.append(current_ki)
    time.sleep(0.5)

# ----------------------------
# PLOT
# ----------------------------
plt.plot(range(1, iterations + 1), ki_values, label='Integral Gain (ki)', color='green', marker='s')
plt.title("Integral Gain (ki) Over 5 Iterations")
plt.xlabel("Iteration")
plt.ylabel("ki Value")
plt.ylim(0, 0.2)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

