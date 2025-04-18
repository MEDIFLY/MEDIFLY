import matplotlib.pyplot as plt
import time

# ----------------------------
# INITIAL SETUP
# ----------------------------
iterations = 5
kp_fixed = 0.5
kp_values = []

print("⚙️ Proportional Gain (kp) Configuration\n")

# ----------------------------
# FRONTEND + BACKEND SIMULATION
# ----------------------------
for i in range(iterations):
    print(f"\n🔁 Iteration {i+1}:")
    current_kp = kp_fixed

    print(f"  🔸 kp value for this iteration: {current_kp}")

    # Backend: Imagine this being sent to your flight controller's PID block
    hardware_packet = {
        "parameter": "kp",
        "value": current_kp
    }

    print(f"  🛠️ Backend Sending → {hardware_packet}")

    # Append to list for plotting
    kp_values.append(current_kp)

    time.sleep(0.5)

# ----------------------------
# PLOT
# ----------------------------
plt.plot(range(1, iterations + 1), kp_values, label='Proportional Gain (kp)', color='blue', marker='o')
plt.title("Proportional Gain (kp) Over 5 Iterations")
plt.xlabel("Iteration")
plt.ylabel("kp Value")
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
