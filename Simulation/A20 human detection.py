import random
import matplotlib.pyplot as plt

# ---------------- FRONTEND: Visual Human Detection at Specific Grid Points ----------------

def visualize_human_detection(grid_size=5):
    detected_points = []
    print("\n🔎 Checking each grid cell for humans using detection function...\n")
    for x in range(grid_size):
        for y in range(grid_size):
            detected = detect_human_at_point(x, y)
            status = "👤" if detected else "❌"
            print(f"📍 Grid ({x}, {y}): {'Human Detected' if detected else 'No Human'}")
            if detected:
                detected_points.append((x, y))

    # Plotting detected human points
    plt.figure(figsize=(6, 6))
    plt.title("🔍 Detected Human Points on Grid")
    plt.xlim(-1, grid_size)
    plt.ylim(-1, grid_size)
    plt.grid(True)
    plt.xticks(range(grid_size))
    plt.yticks(range(grid_size))
    plt.gca().invert_yaxis()

    for x in range(grid_size):
        for y in range(grid_size):
            color = 'red' if (x, y) in detected_points else 'green'
            label = "👤" if (x, y) in detected_points else "❌"
            plt.text(x, y, label, ha='center', va='center', fontsize=14, color='black')
            plt.gca().add_patch(plt.Rectangle((x - 0.5, y - 0.5), 1, 1, edgecolor='black', facecolor=color, alpha=0.3))

    plt.show()

# ---------------- BACKEND: Human Detection Function ----------------

def detect_human_at_point(x, y):
    # In real drone: run AI model / camera data
    # Here: simulate human detection with 40% chance
    return random.random() < 0.4

# ---------------- RUN BOTH FRONTEND + BACKEND ----------------

visualize_human_detection(grid_size=5)
