# ALGORITHM 28: Detection Outcome – Combined Code

import matplotlib.pyplot as plt

# Simulated detection results
iterations = [1, 2, 3, 4, 5]
detection_outcomes = [True, False, True, False, True]

# ---------- Backend: Print Outcomes ----------
print("----- Detection Outcomes (Backend) -----")
for i, outcome in enumerate(detection_outcomes, 1):
    status = "Obstacle Detected" if outcome else "No Obstacle"
    print(f"Iteration {i}: {status}")

# ---------- Frontend: Plot Outcomes ----------
detection_numeric = [1 if d else 0 for d in detection_outcomes]

plt.figure(figsize=(8, 4))
plt.plot(iterations, detection_numeric, marker='o', linestyle='-', color='blue')
plt.xticks(iterations)
plt.yticks([0, 1], ['No Obstacle', 'Obstacle Detected'])
plt.title("Algorithm 28: Detection Outcome Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Detection Result")
plt.grid(True)
plt.tight_layout()
plt.show()
