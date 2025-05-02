# AI Model 2: AI-Based UAV Flight Path Planning

import matplotlib.pyplot as plt
import numpy as np
import random

# FRONTEND: Define map grid and obstacles
grid_size = 20
obstacle_count = 15
start = (0, 0)
end = (19, 19)

# Generate grid with random obstacles
grid = np.zeros((grid_size, grid_size))
for _ in range(obstacle_count):
    x, y = random.randint(1, grid_size - 2), random.randint(1, grid_size - 2)
    grid[x][y] = 1  # obstacle

# A* pathfinding algorithm
from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    visited = set()

    while not open_set.empty():
        _, current = open_set.get()
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        visited.add(current)
        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                if grid[neighbor[0]][neighbor[1]] == 1 or neighbor in visited:
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                    open_set.put((f_score[neighbor], neighbor))
    return []

# Run A* algorithm
path = a_star(grid, start, end)

# Plot path
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap='Greys', origin='lower')
for x, y in path:
    plt.plot(y, x, 'go')  # path in green
plt.plot(start[1], start[0], 'bo')  # start point
plt.plot(end[1], end[0], 'ro')      # end point
plt.title("Planned UAV Flight Path")
plt.grid(True)
plt.show()

# BACKEND: Placeholder for hardware GPS path
def execute_flight_path(path):
    for i, waypoint in enumerate(path):
        print(f"→ Flying to waypoint {i+1}: {waypoint}")
        # Insert GPS hardware navigation logic here
        # E.g., drone.fly_to(waypoint)

# Replace simulate with hardware call in integration
# execute_flight_path(path)
