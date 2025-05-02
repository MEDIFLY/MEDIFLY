# AI Model 5: CMS-Based Collaborative Decision Making

import random
import time
import matplotlib.pyplot as plt

# FRONTEND: Define UAVs and tasks
uavs = ["UAV_A", "UAV_B", "UAV_C", "UAV_D"]
tasks = [
    {"task": "Area Mapping", "priority": 3},
    {"task": "Payload Delivery", "priority": 5},
    {"task": "Thermal Scanning", "priority": 2},
    {"task": "Rescue Signal Relay", "priority": 4}
]

# Sort tasks by priority (high to low)
sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)

# Simulate capability scoring and decision logic
def get_uav_score():
    return random.randint(1, 10)

assigned_tasks = {}

for task in sorted_tasks:
    best_uav = None
    highest_score = -1
    for uav in uavs:
        score = get_uav_score()
        print(f"{uav} voting for task '{task['task']}' with score {score}")
        if score > highest_score:
            best_uav = uav
            highest_score = score
    assigned_tasks[best_uav] = task["task"]
    uavs.remove(best_uav)  # Remove from pool after assignment

# Display assignments
print("\n--- Task Allocation Result ---")
for uav, task in assigned_tasks.items():
    print(f"{uav} → Assigned Task: {task}")

# Plot 1: Task Priorities
task_names = [task["task"] for task in sorted_tasks]
priorities = [task["priority"] for task in sorted_tasks]

plt.figure(figsize=(6, 4))
plt.barh(task_names, priorities, color='teal')
plt.title("Task Priorities")
plt.xlabel("Priority Level")
plt.gca().invert_yaxis()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Plot 2: Final Task Assignment Map
uav_names = list(assigned_tasks.keys())
assigned_task_names = [assigned_tasks[uav] for uav in uav_names]

plt.figure(figsize=(6, 4))
bars = plt.bar(uav_names, range(len(uav_names)), tick_label=uav_names, color='orange')
plt.title("UAV Task Assignments")
plt.ylabel("Task Index")
plt.xticks(rotation=45)

for i, task in enumerate(assigned_task_names):
    plt.text(i, i, task, ha='center', va='bottom', fontsize=9, rotation=90)

plt.tight_layout()
plt.show()

# BACKEND: Feedback acknowledgment and reallocation
def confirm_assignment(uav, task):
    ack = random.choice([True, True, False])  # Simulate random failure
    if ack:
        print(f"{uav} confirms task: {task}")
        return True
    else:
        print(f"{uav} failed to confirm task: {task}")
        return False

# Handle acknowledgments
for uav, task in list(assigned_tasks.items()):
    confirmed = confirm_assignment(uav, task)
    if not confirmed:
        print(f"Reassigning task '{task}'...")
        # Find backup UAV
        for backup_uav in ["UAV_X", "UAV_Y", "UAV_Z"]:
            print(f"Trying reassignment to {backup_uav}")
            if confirm_assignment(backup_uav, task):
                assigned_tasks[backup_uav] = task
                break
        del assigned_tasks[uav]
