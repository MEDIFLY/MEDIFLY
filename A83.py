import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --------- AI Flight Path Adjustment Class (Backend) ---------
class AIFlightControl:
    def __init__(self):
        self.drone_position = np.array([0.0, 0.0, 100.0])  # Float values to avoid dtype errors
        self.wind_vector = np.array([1.0, 1.0, 0.0])       # Wind vector
        self.model = LinearRegression()
        self.history = [self.drone_position.copy()]

    def train_ai_model(self):
        # Training data: simulate known positions and required adjustments
        X = np.array([[0, 0, 100], [5, 5, 100], [-5, -5, 100], [10, 0, 100]])
        y = np.array([[0, 0, 0], [-1, -1, 0], [1, 1, 0], [-2, 0, 0]])
        self.model.fit(X, y)

    def predict_path_adjustment(self):
        # Predict how the drone should adjust based on current position
        prediction = self.model.predict([self.drone_position])
        return prediction[0]

    def adjust_flight_path(self):
        adjustment = self.predict_path_adjustment()
        self.drone_position += adjustment
        self.history.append(self.drone_position.copy())

    def simulate_flight(self, steps=10):
        print("Starting AI-based flight control simulation...\n")
        self.train_ai_model()
        for i in range(steps):
            print(f"Step {i+1}")
            print(f"Current Drone Position: {self.drone_position}")
            self.drone_position += self.wind_vector  # Wind effect
            self.adjust_flight_path()
        print("\nSimulation Complete.")

    def plot_flight_path(self):
        history_array = np.array(self.history)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(history_array[:, 0], history_array[:, 1], history_array[:, 2], label='Flight Path')
        ax.scatter(history_array[0, 0], history_array[0, 1], history_array[0, 2], c='green', label='Start')
        ax.scatter(history_array[-1, 0], history_array[-1, 1], history_array[-1, 2], c='red', label='End')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.set_zlabel('Altitude (Z)')
        ax.set_title('AI-Adjusted Drone Flight Path')
        ax.legend()
        plt.show()

# --------- Execute Both Frontend (Simulation) and Backend ---------
if __name__ == "__main__":
    ai_flight_control = AIFlightControl()
    ai_flight_control.simulate_flight(steps=10)
    ai_flight_control.plot_flight_path()
