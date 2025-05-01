# AI Model 4: MARL-Based Reinforcement Learning for UAVs

import numpy as np
import matplotlib.pyplot as plt
import random

# FRONTEND: Define environment
grid_size = 6
state_space = grid_size * grid_size
action_space = 4  # up, down, left, right
episodes = 200
alpha = 0.1
gamma = 0.9
epsilon = 0.2
num_agents = 2

# Define actions
actions = {
    0: (-1, 0),  # up
    1: (1, 0),   # down
    2: (0, -1),  # left
    3: (0, 1)    # right
}

# Initialize Q-tables
Q_tables = [np.zeros((state_space, action_space)) for _ in range(num_agents)]

# Define reward function and goal
goal = (5, 5)
def state_to_index(x, y): return x * grid_size + y
def is_valid(x, y): return 0 <= x < grid_size and 0 <= y < grid_size

# Training loop
rewards_per_episode = []

for ep in range(episodes):
    positions = [(0, 0) for _ in range(num_agents)]
    done = [False] * num_agents
    total_reward = 0

    while not all(done):
        for agent_id in range(num_agents):
            x, y = positions[agent_id]
            state = state_to_index(x, y)

            # Epsilon-greedy action selection
            if random.random() < epsilon:
                action = random.randint(0, 3)
            else:
                action = np.argmax(Q_tables[agent_id][state])

            dx, dy = actions[action]
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny):
                new_state = state_to_index(nx, ny)
                reward = 100 if (nx, ny) == goal else -1
                Q_tables[agent_id][state][action] += alpha * (
                    reward + gamma * np.max(Q_tables[agent_id][new_state]) - Q_tables[agent_id][state][action]
                )
                positions[agent_id] = (nx, ny)
                total_reward += reward
                if (nx, ny) == goal:
                    done[agent_id] = True

    rewards_per_episode.append(total_reward)

# Plot cumulative rewards
plt.plot(rewards_per_episode)
plt.title("MARL: Total Reward per Episode")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.grid(True)
plt.show()

# BACKEND: Q-table deployment logic
def deploy_q_policy(Q_table, position):
    x, y = position
    state = state_to_index(x, y)
    best_action = np.argmax(Q_table[state])
    move = actions[best_action]
    print(f"Moving UAV from {position} → {(x + move[0], y + move[1])}")
    # Hardware: Convert move to GPS or actuation
