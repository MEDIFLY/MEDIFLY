# A69.py – Algorithm 69: Medicine Payload Drop Mechanism

import matplotlib.pyplot as plt
import time
import random

# ------------------------------
# Frontend Simulation + Visualization
# ------------------------------

# Step 1: Simulate 5 drop statuses
drop_statuses = []

print("\n--- Frontend: Simulating Medicine Payload Drop Mechanism ---")
for i in range(5):
    # Simulate success or failure with 95% success rate
    success = random.choices([True, False], weights=[95, 5])[0]
    drop_statuses.append(success)
    status_text = "✅ Drop Successful" if success else "❌ Drop Failed"
    print(f"Iteration {i+1}: {status_text}")
    time.sleep(0.5)

# Step 2: Plot success/failure for 5 iterations
plt.figure(figsize=(6, 4))
colors = ['green' if s else 'red' for s in drop_statuses]
plt.bar(range(1, 6), [1]*5, color=colors, tick_label=[f'Iter {i+1}' for i in range(5)])
plt.title("Medicine Payload Drop Status (Simulation)")
plt.ylabel("Drop Action")
plt.yticks([])
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# ------------------------------
# Backend Hardware Integration
# ------------------------------

# Simulated Servo Class
class ServoMechanism:
    def __init__(self):
        self.position = "LOCKED"  # initial state

    def release_payload(self):
        print("🔧 Servo: Unlocking payload bay...")
        time.sleep(1)
        self.position = "UNLOCKED"
        print("🧪 Medicine payload dropped!")
        return True

    def reset(self):
        print("🔄 Resetting servo to LOCKED position.")
        self.position = "LOCKED"

# Initialize servo
servo = ServoMechanism()

# Step 3: Perform 5 hardware-controlled drops
print("\n--- Backend: Executing Payload Release via Servo Mechanism ---")
for i in range(5):
    print(f"\nIteration {i+1}:")
    success = servo.release_payload()
    if success:
        print("✅ Drop confirmed by hardware system.")
    else:
        print("❌ Drop failed. Check mechanical issue.")
    servo.reset()
    time.sleep(0.5)
