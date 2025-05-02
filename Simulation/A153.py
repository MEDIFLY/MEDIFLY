import time
import matplotlib.pyplot as plt

# Frontend Simulation: Function to simulate the descent for the payload drop
def simulate_descent_for_payload(position, descent_status):
    """
    Simulate displaying the descent status of the drone during payload drop.
    """
    print(f"Simulating Descent for Payload Drop...")
    print(f"Position: {position}, Descent Status: {descent_status}")

# Backend Logic: Function to simulate the descent for the payload drop
def perform_descent_for_payload(position):
    """
    Function to simulate the descent of the drone for payload drop.
    This involves decreasing the altitude to drop the payload.
    """
    if position[2] > 50:  # Descent happens if the altitude is above 50m
        position[2] -= 1  # Descent by 1 meter each time
        return f"Descent in Progress, Current Altitude: {position[2]}m"
    else:
        return "Descent Complete, Ready for Drop"

# Frontend Plotting: Plot the descent process for the payload drop
def plot_descent_for_payload(position):
    plt.figure()
    plt.plot(position[0], position[1], 'ro')
    plt.title("Drone Descent for Payload Drop")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.show()

# Main loop for Descent for Payload Drop
def descent_for_payload_drop():
    """
    Simulates the descent of the drone and updates the status in both frontend and backend.
    """
    position = [0, 0, 100]  # Starting position at 100m altitude

    for t in range(51):  # Descend 50 meters to the drop point
        # Perform the descent (backend logic)
        descent_status = perform_descent_for_payload(position)

        # Simulate displaying the descent status in the frontend
        simulate_descent_for_payload(position, descent_status)

        # Frontend Plotting: Visualize descent process
        plot_descent_for_payload(position)

        # Print the backend results
        print(f"[Backend] Descent Status: {descent_status}")

        time.sleep(0.2)  # Simulate a small delay between descent steps

    print(f"[Backend] Final Position for Payload Drop: {position}")
# Run the descent for payload drop
if __name__ == "__main__":
    descent_for_payload_drop()
