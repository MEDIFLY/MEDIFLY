# AI Model 14: Hybrid Communication System for UAV Operations

import numpy as np
import matplotlib.pyplot as plt

# FRONTEND: Simulate UAV communication system with multiple protocols
n = 100
time = np.linspace(0, 10, n)
wifi_signal_strength = 100 - 0.5 * np.linspace(0, 1000, n) + np.random.normal(0, 2, n)  # Wi-Fi signal strength
lte_signal_strength = 80 - 0.6 * np.linspace(0, 1000, n) + np.random.normal(0, 3, n)  # LTE signal strength

# Simulate switching mechanism between Wi-Fi and LTE based on signal strength
active_protocol = np.where(wifi_signal_strength > lte_signal_strength, 'Wi-Fi', 'LTE')

# BACKEND: Hybrid communication system decisions
switch_decision = np.zeros(n, dtype=object)
for i in range(1, n):
    if active_protocol[i] != active_protocol[i-1]:
        switch_decision[i] = 'Switch'
    else:
        switch_decision[i] = 'No Switch'

# Print communication status at the final step
print(f"Final Active Protocol: {active_protocol[-1]}")
print(f"Total Switches: {np.sum(switch_decision == 'Switch')}")

# Plot 1: Signal Strength Comparison (Wi-Fi vs LTE)
plt.figure(figsize=(8, 4))
plt.plot(wifi_signal_strength, label='Wi-Fi Signal Strength', color='blue')
plt.plot(lte_signal_strength, label='LTE Signal Strength', color='red')
plt.title("Signal Strength Comparison (Wi-Fi vs LTE)")
plt.xlabel("Distance (m)")
plt.ylabel("Signal Strength")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Protocol Switching Events
plt.figure(figsize=(8, 4))
switches = [1 if decision == 'Switch' else 0 for decision in switch_decision]
plt.plot(switches, label='Protocol Switch', color='green')
plt.title("Protocol Switching Events")
plt.xlabel("Time (s)")
plt.ylabel("Switch Event")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
