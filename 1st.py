
# Program to determine the nth roots of a complex number
# and represent them in Cartesian and Polar forms.

import cmath
import math


# Function to calculate nth roots of a complex number
def find_nth_roots(z, n):

    # Step 1: Find modulus and argument
    r = abs(z)
    theta = cmath.phase(z)

    # Step 2: Calculate modulus of each root
    root_modulus = r ** (1 / n)

    print("\nOriginal Complex Number:", z)
    print("Modulus (r):", r)
    print("Argument (theta):", theta, "radians")

    print("\nThe", n, "th roots are:\n")

    # Step 3: Calculate all nth roots
    for k in range(n):

        # Calculate angle of each root
        angle = (theta + 2 * math.pi * k) / n

        # Step 4: Calculate root in polar form
        real_part = root_modulus * math.cos(angle)
        imag_part = root_modulus * math.sin(angle)

        # Step 5: Calculate root in Cartesian form
        root = complex(real_part, imag_part)

        # Display results
        print("Root", k + 1)

        print("Polar Form:")
        print(f"{root_modulus:.4f} "
              f"[cos({angle:.4f}) + i sin({angle:.4f})]")

        print("Cartesian Form:")
        print(f"{real_part:.4f} + ({imag_part:.4f})i")

        print("-" * 40)


# Main program
def main():

    print("NTH ROOTS OF A COMPLEX NUMBER")
    print("--------------------------------")

    # Input real and imaginary parts
    a = float(input("Enter real part: "))
    b = float(input("Enter imaginary part: "))

    # Input value of n
    n = int(input("Enter the value of n: "))

    # Validate input
    if n <= 0:
        print("Error: n must be a positive integer.")
        return

    # Create complex number
    z = complex(a, b)

    # Calculate roots
    find_nth_roots(z, n)


# Execute main function
if __name__ == "__main__":
    main()
