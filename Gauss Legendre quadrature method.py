
# Gauss-Legendre Quadrature and
# Representation using Legendre Polynomials

import math


# Function to calculate Legendre polynomial
def legendre(n, x):

    if n == 0:
        return 1

    if n == 1:
        return x

    p0 = 1
    p1 = x

    for k in range(2, n + 1):

        p2 = ((2*k - 1)*x*p1 -
              (k - 1)*p0) / k

        p0 = p1
        p1 = p2

    return p1


# Function to calculate roots and weights
def gauss_legendre(n):

    roots = []
    weights = []

    for i in range(1, n + 1):

        x = math.cos(math.pi *
                     (i - 0.25) / (n + 0.5))

        # Newton-Raphson iteration
        for j in range(100):

            p = legendre(n, x)

            dp = n * (x*p - legendre(n-1, x)) / (
                x*x - 1
            )

            dx = p / dp
            x = x - dx

            if abs(dx) < 1e-12:
                break

        # Calculate weight
        p = legendre(n, x)

        dp = n * (x*p - legendre(n-1, x)) / (
            x*x - 1
        )

        w = 2 / ((1 - x*x) * dp*dp)

        roots.append(x)
        weights.append(w)

    return roots, weights


# Function to perform Gauss-Legendre integration
def integrate(f, a, b, n):

    roots, weights = gauss_legendre(n)

    result = 0

    for i in range(n):

        # Transform interval [-1,1] to [a,b]
        x = ((b-a)*roots[i] + (b+a)) / 2

        result += weights[i] * f(x)

    result = result * (b-a) / 2

    return result


# Function to calculate Legendre coefficients
def coefficients(f, N, n):

    coeff = []

    for k in range(N + 1):

        integral = integrate(
            lambda x: f(x)*legendre(k, x),
            -1, 1, n
        )

        a_k = ((2*k + 1)/2) * integral

        coeff.append(a_k)

    return coeff


# Main program
def main():

    # Define the function
    f = lambda x: math.exp(x)

    a = -1
    b = 1

    # Number of quadrature points
    n = 5

    # Number of Legendre polynomials
    N = 4

    # Calculate definite integral
    result = integrate(f, a, b, n)

    print("\nGAUSS-LEGENDRE QUADRATURE")
    print("--------------------------------")

    print("Integral of e^x from -1 to 1:")
    print(f"Numerical result = {result:.10f}")

    # Exact result
    exact = math.e - 1/math.e

    print(f"Exact result = {exact:.10f}")

    print(f"Absolute error = {abs(exact-result):.10e}")

    # Calculate Legendre coefficients
    coeff = coefficients(f, N, n)

    print("\nLEGENDRE POLYNOMIAL EXPANSION")
    print("--------------------------------")

    for k in range(N + 1):
        print(f"Coefficient a{k} = {coeff[k]:.6f}")

    # Display complete function representation
    print("\nFUNCTION REPRESENTATION")
    print("--------------------------------")

    terms = []

    for k in range(N + 1):

        if abs(coeff[k]) > 1e-10:
            terms.append(
                f"({coeff[k]:.6f}) P_{k}(x)"
            )

    print("f(x) ≈ " + " + ".join(terms))

    # Display expanded polynomial form
    print("\nEXPANDED POLYNOMIAL FORM")
    print("--------------------------------")

    print(
        f"f(x) ≈ {coeff[0]:.6f}\n"
        f"     + ({coeff[1]:.6f})x\n"
        f"     + ({coeff[2]:.6f})[(3x^2 - 1)/2]\n"
        f"     + ({coeff[3]:.6f})[(5x^3 - 3x)/2]\n"
        f"     + ({coeff[4]:.6f})[(35x^4 - 30x^2 + 3)/8]"
    )

    # Reconstruct function at x = 0.5
    x = 0.5

    approximation = 0

    for k in range(N + 1):
        approximation += coeff[k] * legendre(k, x)

    print("\nFUNCTION APPROXIMATION")
    print("--------------------------------")

    print(f"At x = {x}")
    print(f"Actual function value = {f(x):.6f}")
    print(f"Approximated value = {approximation:.6f}")


# Execute main program
if __name__ == "__main__":
    main()
