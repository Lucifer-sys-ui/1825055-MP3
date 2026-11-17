
import numpy as np
import matplotlib.pyplot as plt

# Display available functions
print("COMPLEX FUNCTION MAPPING")
print("1. Identity       w = z")
print("2. Square         w = z^2")
print("3. Cube           w = z^3")
print("4. Exponential    w = exp(z)")
print("5. Reciprocal     w = 1/z")
print("6. Sine           w = sin(z)")

choice = int(input("\nEnter your choice (1-6): "))

# User-defined plotting range
xmin = float(input("Enter minimum real value: "))
xmax = float(input("Enter maximum real value: "))

ymin = float(input("Enter minimum imaginary value: "))
ymax = float(input("Enter maximum imaginary value: "))

N = int(input("Enter grid resolution (e.g. 30): "))

if N < 2 or xmin >= xmax or ymin >= ymax:
    raise ValueError("Invalid range or grid resolution.")

# Create complex grid
x = np.linspace(xmin, xmax, N)
y = np.linspace(ymin, ymax, N)

X, Y = np.meshgrid(x, y)

Z = X + 1j * Y

# Apply selected complex function
if choice == 1:
    W = Z
    function_name = "w = z"

elif choice == 2:
    W = Z**2
    function_name = "w = z^2"

elif choice == 3:
    W = Z**3
    function_name = "w = z^3"

elif choice == 4:
    W = np.exp(Z)
    function_name = "w = exp(z)"

elif choice == 5:
    W = np.divide(
        1, Z,
        out=np.full(Z.shape, np.nan + 1j*np.nan),
        where=(np.abs(Z) > 1e-10)
    )
    function_name = "w = 1/z"

elif choice == 6:
    W = np.sin(Z)
    function_name = "w = sin(z)"

else:
    raise ValueError("Invalid function choice.")

# Extract real and imaginary parts
U = W.real
V = W.imag

# Plot z-plane and w-plane
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Original z-plane
axes[0].scatter(
    Z.real.flatten(),
    Z.imag.flatten(),
    s=5,
    color='blue'
)

axes[0].set_title("Original z-plane")
axes[0].set_xlabel("Real(z)")
axes[0].set_ylabel("Imaginary(z)")
axes[0].grid(True)
axes[0].set_aspect('equal', adjustable='box')

# Transformed w-plane
axes[1].scatter(
    U.flatten(),
    V.flatten(),
    c=np.angle(Z).flatten(),
    cmap='hsv',
    s=5
)

axes[1].set_title("Mapped w-plane: " + function_name)
axes[1].set_xlabel("Real(w)")
axes[1].set_ylabel("Imaginary(w)")
axes[1].grid(True)
axes[1].set_aspect('equal', adjustable='datalim')

plt.tight_layout()
plt.show()

print("\nMapping completed successfully!")
print("Selected function:", function_name)
