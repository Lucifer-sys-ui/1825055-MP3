
# Computation of Discrete Fourier Transform (DFT)
# Using Complex Numbers

import math
import cmath


# Function to calculate DFT
def calculate_dft(signal):

    N = len(signal)

    X = []

    for k in range(N):

        total = 0

        for n in range(N):

            angle = -2 * math.pi * k * n / N

            # Complex exponential
            W = cmath.exp(1j * angle)

            total += signal[n] * W

        X.append(total)

    return X


# Function to calculate Inverse DFT
def calculate_idft(X):

    N = len(X)

    signal = []

    for n in range(N):

        total = 0

        for k in range(N):

            angle = 2 * math.pi * k * n / N

            W = cmath.exp(1j * angle)

            total += X[k] * W

        signal.append(total / N)

    return signal


# Main program
def main():

    print("\nDISCRETE FOURIER TRANSFORM")
    print("================================")

    # Input discrete signal
    N = int(input("Enter number of samples: "))

    if N <= 0:
        print("Number of samples must be positive.")
        return

    signal = []

    print("\nEnter signal values:")

    for i in range(N):

        value = float(input(f"x({i}) = "))

        signal.append(value)

    # Calculate DFT
    X = calculate_dft(signal)

    # Display input signal
    print("\nINPUT SIGNAL")
    print("--------------------------------")

    print(signal)

    # Display DFT coefficients
    print("\nDFT COEFFICIENTS")
    print("--------------------------------")

    for k in range(N):

        print(f"X({k}) = {X[k].real:.4f} "
              f"+ ({X[k].imag:.4f})i")

    # Display magnitude and phase
    print("\nMAGNITUDE AND PHASE SPECTRUM")
    print("--------------------------------")

    for k in range(N):

        magnitude = abs(X[k])

        phase = cmath.phase(X[k])

        print(f"X({k}): Magnitude = {magnitude:.4f}, "
              f"Phase = {phase:.4f} radians")

    # Calculate inverse DFT
    reconstructed = calculate_idft(X)

    # Display reconstructed signal
    print("\nRECONSTRUCTED SIGNAL")
    print("--------------------------------")

    for n in range(N):

        print(f"x({n}) = {reconstructed[n].real:.4f}")

    print("\nDFT COMPUTATION COMPLETED")


# Execute main program
if __name__ == "__main__":
    main()
