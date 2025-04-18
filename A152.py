import time
import matplotlib.pyplot as plt

# Frontend Simulation: Function to display the details of the drop execution
def simulate_drop_execution_details(position, drop_status):
    """
    Simulate displaying the details of the drop execution.
    """
    print(f"Simulating Drop Execution...")
    print(f"Position: {position}, Drop Status: {drop_status}")

# Backend Logic: Function to perform the drop execution and update its status
def perform_drop_execution(position):
    """
    Function to simulate the drop execution.
    In a real system, this would involve controlling a mechanism to release the payload.
    Here we simulate success if position is at drop altitude (100m).
    """
    if position[2] == 100:  # At 100m altitude, drop the payload
        return "Drop Executed"
    else:
        return "Drop Failed"

# Frontend Plotting: Plot the drone's position during the drop execution
def plot_drop_execution(position):
    plt.figure()
    plt.plot(position[0], position[1], 'bo')
    plt.title("Drone Drop Execution")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.show()

# Main loop for Drop Execution Details
def drop_execution_details():
    """
    Executes the drop execution, simulating the frontend and backend behavior.
    """
    position = [0, 0, 100]  # Starting position at 100m altitude
    drop_status = None
    
    for t in range(5):  # Limiting to 5 iterations for quick testing
        # Perform the drop execution (backend logic)
        drop_status = perform_drop_execution(position)

        # Simulate displaying the drop execution details in the frontend
        simulate_drop_execution_details(position, drop_status)

        # Frontend Plotting: Visualize drop execution
        plot_drop_execution(position)

        # Print the backend results
        print(f"[Backend] Drop Status: {drop_status}")

        # If drop failed, corrective action may be needed
        if drop_status == "Drop Failed":
            print("[Backend] Drop execution failed. Checking altitude...")
        
        time.sleep(0.5)  # Simulate a small delay between checks

# Run the drop execution details
if __name__ == "__main__":
    drop_execution_details()
