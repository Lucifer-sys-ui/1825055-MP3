
import numpy as np
import matplotlib.pyplot as plt

# Number of points
N = 1024

# Define x range
x = np.linspace(-10, 10, N)
dx = x[1] - x[0]

# Given function
f = np.exp(-x**2)

# Numerical Fourier Transform
F = np.fft.fft(f) * dx

# Angular frequency
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)

# Shift FFT and frequency
F = np.fft.fftshift(F)
k = np.fft.fftshift(k)

# Exact analytical Fourier Transform
F_exact = np.sqrt(np.pi) * np.exp(-k**2 / 4)

# Plot original function
plt.figure(figsize=(10, 9))

plt.subplot(3, 1, 1)
plt.plot(x, f)
plt.title("Original Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()

# Plot numerical FFT
plt.subplot(3, 1, 2)
plt.plot(k, np.abs(F), label="Numerical FFT")
plt.title("Numerical Fourier Transform")
plt.xlabel("Angular frequency k")
plt.ylabel("|F(k)|")
plt.grid()
plt.legend()

# Compare numerical and analytical results
plt.subplot(3, 1, 3)
plt.plot(k, np.abs(F), label="Numerical FFT")
plt.plot(k, F_exact, '--', label="Analytical result")
plt.title("Comparison of Fourier Transforms")
plt.xlabel("Angular frequency k")
plt.ylabel("F(k)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Print tabulated values
print("Frequency      Numerical FFT     Analytical FFT")

for i in range(0, N, 100):
    print(f"{k[i]:10.4f}  {abs(F[i]):14.6f}  {F_exact[i]:14.6f}")
