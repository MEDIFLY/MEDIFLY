import matplotlib.pyplot as plt
import numpy as np
import random

# ------------- BACKEND: Human Detection Logic -------------
def detect_humans(grid_size=100, num_humans=10):
    humans = []
    for _ in range(num_humans):
        x = random.randint(10, 90)
        y = random.randint(10, 90)
        # Assume humans are only on ground (no trees or buildings)
        humans.append((x, y))
    return humans

# ------------- FRONTEND: Realistic Visualization -------------
def plot_environment_with_humans(humans):
    grid_size = 100
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_title("Realistic Human Detection from Drone View", fontsize=15)
    ax.set_xlabel("X Position (meters)")
    ax.set_ylabel("Y Position (meters)")

    # Add grass/ground
    ax.add_patch(plt.Rectangle((0, 0), grid_size, grid_size, color='lightgreen'))

    # Add trees (dark green circles)
    for _ in range(15):
        tx, ty = random.randint(0, grid_size), random.randint(0, grid_size)
        tree = plt.Circle((tx, ty), 2.5, color='darkgreen')
        ax.add_patch(tree)

    # Add buildings (gray rectangles)
    for _ in range(5):
        bx, by = random.randint(10, 80), random.randint(10, 80)
        bw, bh = random.randint(5, 10), random.randint(5, 10)
        building = plt.Rectangle((bx, by), bw, bh, color='gray')
        ax.add_patch(building)

    # Plot detected humans (red dots)
    for (x, y) in humans:
        ax.plot(x, y, 'ro', markersize=8)
        ax.text(x + 1, y + 1, "Human", fontsize=9, color='red')

    plt.grid(True)
    plt.show()

# ---------------------- EXECUTION ----------------------
print("🚁 Detecting humans in environment...")
detected_humans = detect_humans()
plot_environment_with_humans(detected_humans)
