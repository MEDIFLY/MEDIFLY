import random
import matplotlib.pyplot as plt

# ---------------- FRONTEND: Survey Simulation and Human Detection Grid Plot ----------------

def simulate_survey_and_detection(area_size=5):
    print("\n🔍 Starting Survey Over Grid Area...")
    grid = []
    for i in range(area_size):
        row = []
        for j in range(area_size):
            human_present = random.choice([True, False])
            status = "👤" if human_present else "❌"
            row.append(status)
            print(f"📍 Grid ({i}, {j}) - {'Detected Human' if human_present else 'Clear'}")
        grid.append(row)

    # Visualization of Grid (Human presence vs no human)
    fig, ax = plt.subplots()
    ax.set_title("👁️‍🗨️ Human Detection Grid Map")
    ax.set_xticks(range(area_size))
    ax.set_yticks(range(area_size))

    for i in range(area_size):
        for j in range(area_size):
            color = 'red' if grid[i][j] == "👤" else 'green'
            ax.text(j, area_size - i - 1, grid[i][j], ha='center', va='center', fontsize=14, color='black')
            ax.add_patch(plt.Rectangle((j - 0.5, area_size - i - 1 - 0.5), 1, 1, edgecolor='black', facecolor=color, alpha=0.3))

    ax.set_xlim(-0.5, area_size - 0.5)
    ax.set_ylim(-0.5, area_size - 0.5)
    ax.set_aspect('equal')
    plt.grid(True)
    plt.show()

# ---------------- BACKEND: Survey Trigger Function ----------------

def start_survey_backend():
    print("🛠️ Backend: Starting human detection survey task...")
    # Could include GPS mapping, camera activation, etc.
    return True

# ---------------- RUN BOTH FRONTEND + BACKEND ----------------

if start_survey_backend():
    simulate_survey_and_detection(area_size=5)
