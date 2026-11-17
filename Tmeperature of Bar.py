
import numpy as np
import matplotlib.pyplot as plt

# Given values
L = 10
T1 = 100
T2 = 0

# Divide the bar into 100 equal points
x = np.linspace(0, L, 100)

# Calculate equilibrium temperature
T = T1 + ((T2 - T1) / L) * x

# Display tabulated values
print("Position (x)    Temperature (T)")
for i in range(0, 100, 10):
    print(f"{x[i]:8.2f}        {T[i]:8.2f}")

# Plot temperature distribution
plt.plot(x, T, color='blue', linewidth=2)

plt.title("Equilibrium Temperature Distribution")
plt.xlabel("Position along the bar (x)")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.show()
