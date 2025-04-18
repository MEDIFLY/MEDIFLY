import random
import matplotlib.pyplot as plt

class Motor:
    def __init__(self, motor_id):
        self.motor_id = motor_id
        self.thrust = 0  # Motor thrust in Newtons
        self.max_thrust = 15  # Max thrust the motor can generate in Newtons

    def initialize_motor(self):
        """Initialize the motor with a random thrust value within its range."""
        self.thrust = random.uniform(5, self.max_thrust)  # Random thrust value between 5 and max_thrust
        print(f"Motor {self.motor_id} Initialized with thrust: {self.thrust:.2f} N")

# --- Main Execution ---
if __name__ == "__main__":
    # Initialize motors for the drone
    motor1 = Motor("MOTOR-1")
    motor2 = Motor("MOTOR-2")
    motor3 = Motor("MOTOR-3")
    motor4 = Motor("MOTOR-4")
    
    # Initialize all motors
    motor1.initialize_motor()
    motor2.initialize_motor()
    motor3.initialize_motor()
    motor4.initialize_motor()
    
    # Prepare data for plotting
    motor_ids = ["MOTOR-1", "MOTOR-2", "MOTOR-3", "MOTOR-4"]
    motor_thrusts = [motor1.thrust, motor2.thrust, motor3.thrust, motor4.thrust]
    
    # Plotting the motor thrust values
    plt.bar(motor_ids, motor_thrusts, color='lightcoral')
    plt.xlabel('Motor ID')
    plt.ylabel('Motor Thrust (N)')
    plt.title('Motor Initialization')
    plt.show()
