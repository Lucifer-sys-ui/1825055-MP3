
import numpy as np
import matplotlib.pyplot as plt

# User-defined inputs
N = int(input("Enter number of grid points (minimum 3): "))

if N < 3:
    raise ValueError("Grid size must be at least 3.")

top = float(input("Enter top boundary temperature: "))
bottom = float(input("Enter bottom boundary temperature: "))
left = float(input("Enter left boundary temperature: "))
right = float(input("Enter right boundary temperature: "))

tolerance = float(input("Enter convergence tolerance (e.g. 0.0001): "))

if tolerance <= 0:
    raise ValueError("Tolerance must be positive.")

# Initialize temperature matrix
T = np.zeros((N, N))

# Apply boundary conditions
T[0, :] = top
T[-1, :] = bottom
T[:, 0] = left
T[:, -1] = right

# Set corner temperatures as averages
T[0, 0] = (top + left) / 2
T[0, -1] = (top + right) / 2
T[-1, 0] = (bottom + left) / 2
T[-1, -1] = (bottom + right) / 2

# Gauss-Seidel iterative method
max_iterations = 10000

for iteration in range(max_iterations):

    max_error = 0

    for i in range(1, N-1):
        for j in range(1, N-1):

            old = T[i, j]

            T[i, j] = 0.25 * (
                T[i+1, j] +
                T[i-1, j] +
                T[i, j+1] +
                T[i, j-1]
            )

            error = abs(T[i, j] - old)

            max_error = max(max_error, error)

    if max_error < tolerance:
        break

# Display results
print("\nTemperature Distribution:")
print(np.round(T, 3))

if iteration < max_iterations - 1:
    print("\nSolution converged!")
else:
    print("\nMaximum iterations reached.")

print("Number of iterations:", iteration + 1)

# Plot temperature distribution
plt.figure(figsize=(8, 6))

plt.imshow(T, cmap='hot', origin='upper',
           interpolation='bilinear')

plt.colorbar(label='Temperature')
plt.title("Numerical Solution of Laplace Equation")
plt.xlabel("X Grid Points")
plt.ylabel("Y Grid Points")

plt.show()

# 3D surface plot
x, y = np.meshgrid(range(N), range(N))

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, T, cmap='viridis')

ax.set_title("Temperature Distribution (3D)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Temperature")

plt.show()
