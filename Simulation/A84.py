import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# --------- AI-Based Flight Control System (Backend) ---------
class AIBasedFlightControl:
    def __init__(self):
        self.position = np.array([0.0, 0.0, 100.0])
        self.wind = np.array([0.5, 0.5, 0.0])
        self.model = DecisionTreeRegressor()
        self.path = [self.position.copy()]

    def train_ai_model(self):
        # Sample training data: drone positions and needed correction
        X_train = np.array([[0, 0, 100], [2, 2, 100], [-2, -2, 100], [3, -3, 100]])
        y_train = np.array([[0, 0, 0], [-0.5, -0.5, 0], [0.5, 0.5, 0], [-1, 1, 0]])
        self.model.fit(X_train, y_train)

    def predict_adjustment(self):
        correction = self.model.predict([self.position])[0]
        return correction

    def adjust_position(self):
        adjustment = self.predict_adjustment()
        self.position += adjustment
        self.path.append(self.position.copy())

    def simulate(self, steps=10):
        print("Starting AI-based decision tree flight control...\n")
        self.train_ai_model()
        for step in range(steps):
            print(f"Step {step + 1} - Position: {self.position}")
            self.position += self.wind  # Wind drift
            self.adjust_position()
        print("\nSimulation complete.")

    def plot_path(self):
        path_array = np.array(self.path)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(path_array[:, 0], path_array[:, 1], path_array[:, 2], label='AI Path')
        ax.scatter(path_array[0, 0], path_array[0, 1], path_array[0, 2], color='green', label='Start')
        ax.scatter(path_array[-1, 0], path_array[-1, 1], path_array[-1, 2], color='red', label='End')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z (Altitude)")
        ax.set_title("AI Decision Tree Adjusted Drone Path")
        ax.legend()
        plt.show()

# --------- Run Simulation ---------
if __name__ == "__main__":
    flight_control = AIBasedFlightControl()
    flight_control.simulate(steps=10)
    flight_control.plot_path()
