import random
import matplotlib.pyplot as plt
import time

class MedicalEquipmentParameters:
    def __init__(self):
        self.time_data = []
        self.equipment_weight = []
        self.equipment_battery = []
        self.initial_weight = 3.0  # Initial weight of the medical equipment in kg
        self.initial_battery = 100  # Initial battery life percentage
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate medical equipment parameters such as weight and battery life."""
        for t in range(self.simulation_time):
            # Simulate weight changes (e.g., battery drain or additional items added)
            self.initial_weight = max(2.5, random.uniform(2.5, 3.5))

            # Simulate battery life drain
            self.initial_battery = max(10, self.initial_battery - random.uniform(0.5, 1.5))

            # Store data for plotting
            self.time_data.append(t)
            self.equipment_weight.append(self.initial_weight)
            self.equipment_battery.append(self.initial_battery)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Simulation with medical equipment parameters complete.")

    def plot_medical_equipment_parameters(self):
        """Plot medical equipment weight and battery life over time."""
        plt.figure(figsize=(10, 6))

        # Plot weight changes
        plt.subplot(2, 1, 1)
        plt.plot(self.time_data, self.equipment_weight, label="Medical Equipment Weight (kg)", color='tab:orange')
        plt.title("Medical Equipment Weight Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Weight (kg)")
        plt.legend()

        # Plot battery life changes
        plt.subplot(2, 1, 2)
        plt.plot(self.time_data, self.equipment_battery, label="Medical Equipment Battery (%)", color='tab:purple')
        plt.title("Medical Equipment Battery Life Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Battery Life (%)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    medical_equipment_params = MedicalEquipmentParameters()
    medical_equipment_params.run_simulation()
    medical_equipment_params.plot_medical_equipment_parameters()
