import matplotlib.pyplot as plt
import time

# ----------------------------
# PARAMETERS
# ----------------------------
iterations = 5

# PID Parameters (fixed for all iterations)
kp = 0.5  # Proportional Gain
ki = 0.1  # Integral Gain
kd = 0.01  # Derivative Gain

# Store history for plot
kp_list, ki_list, kd_list = [], [], []

print("🧠 PID Controller Parameters for Hover Control\n")

# ----------------------------
# SIMULATION + BACKEND LOGIC
# ----------------------------
for i in range(iterations):
    print(f"\n🔁 Iteration {i+1}:")

    # Here we simulate (for now, fixed values — later these may vary or adapt using AI)
    current_kp = kp
    current_ki = ki
    current_kd = kd

    print(f"  🔸 kp (Proportional Gain): {current_kp}")
    print(f"  🔸 ki (Integral Gain): {current_ki}")
    print(f"  🔸 kd (Derivative Gain): {current_kd}")

    # Backend placeholder: use gains to send to motor controller (future real-time control)
    # For now, we simulate adding them to hardware control queue
    motor_control_data = {
        "P": current_kp,
        "I": current_ki,
        "D": current_kd
    }

    print(f"  🛠️ Sending to controller → {motor_control_data}")

    # Store for plotting
    kp_list.append(current_kp)
    ki_list.append(current_ki)
    kd_list.append(current_kd)

    time.sleep(0.5)

# ----------------------------
# PLOTTING SECTION
# ----------------------------
x_axis = list(range(1, iterations + 1))
plt.plot(x_axis, kp_list, label="Proportional Gain (kp)", marker='o')
plt.plot(x_axis, ki_list, label="Integral Gain (ki)", marker='s')
plt.plot(x_axis, kd_list, label="Derivative Gain (kd)", marker='^')

plt.title("PID Gain Parameters Across 5 Iterations")
plt.xlabel("Iteration")
plt.ylabel("Gain Value")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

