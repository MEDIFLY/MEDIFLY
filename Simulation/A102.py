import matplotlib.pyplot as plt
import time

# Initialize PID gains
kp = 0.6
ki = 0.2
kd = 0.05

# Initialize errors and state
setpoint = 10  # target altitude in meters
current_altitude = 0
error_sum = 0
error_prev = 0
control_output_log = []
iteration_log = []

print("🧮 Starting Algorithm 102: Control Output Calculation...")

# 🧪 FRONTEND: 5 Simulation Iterations
for i in range(5):
    print(f"\n🔁 Iteration {i+1}")
    error = setpoint - current_altitude
    error_sum += error
    error_diff = error - error_prev

    control_output = (kp * error) + (ki * error_sum) + (kd * error_diff)
    print(f"  ➤ Error: {error:.2f}")
    print(f"  ➤ Control Output: {control_output:.2f}")

    # Simulate drone response (assume control output directly affects altitude)
    current_altitude += control_output * 0.1
    error_prev = error

    # Log for plotting
    control_output_log.append(control_output)
    iteration_log.append(i + 1)

    # Simulated delay
    time.sleep(0.5)

# 📊 Plotting
plt.figure(figsize=(10, 5))
plt.plot(iteration_log, control_output_log, marker='o', linestyle='--', color='purple', linewidth=2)
plt.title('Control Output Over Iterations (A102)')
plt.xlabel('Iteration')
plt.ylabel('Control Output')
plt.grid(True)
plt.show()

# 🧠 BACKEND: Hardware Control Logic
def calculate_pid_control(current_altitude, setpoint, kp, ki, kd, error_prev, error_sum):
    error = setpoint - current_altitude
    error_sum += error
    error_diff = error - error_prev
    control_output = (kp * error) + (ki * error_sum) + (kd * error_diff)
    return control_output, error_sum, error

# Example hardware call
current_altitude = 7.2
setpoint = 10
output, updated_sum, updated_prev = calculate_pid_control(current_altitude, setpoint, kp, ki, kd, error_prev, error_sum)
print("\n⚙️ Backend Hardware Control Output:", round(output, 2))
