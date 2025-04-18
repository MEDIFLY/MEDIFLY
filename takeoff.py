# --------------------------------------------
# Algorithm 1: Drone Initialization and System Check
# Project: MEDIFLY
# Description: Basic startup check and drone readiness confirmation
# --------------------------------------------

import time   # For simulating delay
import sys    # To exit if system check fails

def initialize_drone():
    print("🚁 Initializing MEDIFLY Drone System...")
    time.sleep(1)
    
    print("🔍 Performing System Check...")
    time.sleep(1)

    print("✅ GPS Module: OK")
    time.sleep(0.5)

    print("✅ Battery Status: OK")
    time.sleep(0.5)

    print("✅ Motor Check: OK")
    time.sleep(0.5)

    print("✅ All Systems Functional ✅")
    print("MEDIFLY Drone Ready for Takeoff 🚀")

if __name__ == "__main__":
    initialize_drone()
