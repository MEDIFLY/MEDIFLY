import random
import matplotlib.pyplot as plt

# ---------------- FRONTEND: Voice Detection Plot ----------------
def simulate_voice_detection_plot(command):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Drone Voice Detection and Relay", fontsize=14)
    
    # Simulate drone and person locations
    drone_pos = (5, 9)
    human_pos = (5, 1)
    
    ax.plot(*drone_pos, 'bo', markersize=10, label="Drone")
    ax.plot(*human_pos, 'ro', markersize=10, label="Human")

    # Draw arrow showing voice relay
    ax.annotate("",
                xy=drone_pos, xycoords='data',
                xytext=human_pos, textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=2, color='orange'))
    
    ax.text(3.5, 5, f'Voice Command: "{command}"', fontsize=12, color='purple', bbox=dict(facecolor='yellow', alpha=0.5))
    
    ax.legend()
    ax.grid(True)
    plt.show()
    
# ---------------- BACKEND: Voice Retrieval and Relay Logic ----------------
def retrieve_voice_command():
    voice_commands = ["Help!", "Food!", "Water!", "Medicine!", "Rescue!"]
    detected_command = random.choice(voice_commands)
    return detected_command

def relay_command_to_control_center(command):
    print(f"📡 Relaying command to control center: \"{command}\"")

# ---------------- EXECUTION ----------------
print("🎙️ Detecting voice from survivor...")
command = retrieve_voice_command()
simulate_voice_detection_plot(command)
relay_command_to_control_center(command)
