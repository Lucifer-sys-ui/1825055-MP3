
import numpy as np
import matplotlib.pyplot as plt

# User input for complex number
x = float(input("Enter the real part: "))
y = float(input("Enter the imaginary part: "))

z = complex(x, y)

print("\nOriginal Complex Number:", z)

# 1. Translation
print("\n--- Translation ---")
a = float(input("Enter translation along real axis: "))
b = float(input("Enter translation along imaginary axis: "))

z_translation = z + complex(a, b)

# 2. Scaling
print("\n--- Scaling ---")
s = float(input("Enter scaling factor: "))

z_scaling = s * z

# 3. Rotation
print("\n--- Rotation ---")
angle = float(input("Enter rotation angle in degrees: "))

theta = np.radians(angle)
z_rotation = z * np.exp(1j * theta)

# 4. Reflection
print("\n--- Reflection ---")
print("1. Real axis")
print("2. Imaginary axis")
choice = int(input("Choose reflection axis (1 or 2): "))

if choice == 1:
    z_reflection = np.conjugate(z)
    reflection_name = "Reflection about Real Axis"

elif choice == 2:
    z_reflection = -np.conjugate(z)
    reflection_name = "Reflection about Imaginary Axis"

else:
    print("Invalid choice. Defaulting to real axis.")
    z_reflection = np.conjugate(z)
    reflection_name = "Reflection about Real Axis"

# Display results
print("\n===== TRANSFORMATION RESULTS =====")
print("Original:", z)
print("Translation:", z_translation)
print("Scaling:", z_scaling)
print("Rotation:", np.round(z_rotation, 5))
print("Reflection:", z_reflection)

# Plotting
points = [
    (z, "Original"),
    (z_translation, "Translation"),
    (z_scaling, "Scaling"),
    (z_rotation, "Rotation"),
    (z_reflection, "Reflection")
]

colors = ['black', 'red', 'green', 'blue', 'purple']

plt.figure(figsize=(10, 8))

for (point, label), color in zip(points, colors):

    plt.quiver(
        0, 0,
        point.real, point.imag,
        angles='xy',
        scale_units='xy',
        scale=1,
        color=color,
        label=label
    )

    plt.text(point.real, point.imag, label)

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')

plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("User-Defined Complex Number Transformations")

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
