
# Improper Integration using
# Gauss-Laguerre and Gauss-Hermite Quadrature

import math


# -----------------------------------------
# PART A: GAUSS-LAGUERRE QUADRATURE
# -----------------------------------------

# Function to calculate Laguerre polynomial
def laguerre(n, x):

    if n == 0:
        return 1.0

    if n == 1:
        return 1.0 - x

    p0 = 1.0
    p1 = 1.0 - x

    for k in range(2, n + 1):

        p2 = ((2*k - 1 - x)*p1 -
              (k - 1)*p0) / k

        p0 = p1
        p1 = p2

    return p1


# Function to find roots using bisection
def find_roots(poly, low, high, step):

    roots = []

    x1 = low
    y1 = poly(x1)

    while x1 < high:

        x2 = min(x1 + step, high)
        y2 = poly(x2)

        if y1 * y2 < 0:

            left = x1
            right = x2

            # Bisection iteration
            for _ in range(60):

                mid = (left + right) / 2

                if poly(left) * poly(mid) <= 0:
                    right = mid
                else:
                    left = mid

            root = (left + right) / 2

            if not roots or abs(root-roots[-1]) > 1e-7:
                roots.append(root)

        x1 = x2
        y1 = y2

    return roots


# Calculate Laguerre roots and weights
def laguerre_points(n):

    roots = find_roots(
        lambda x: laguerre(n, x),
        0.0, max(30.0, 5.0*n), 0.01
    )

    if len(roots) != n:
        raise ValueError("Unable to locate all Laguerre roots.")

    weights = []

    for x in roots:

        p = laguerre(n+1, x)

        w = x / ((n+1)**2 * p**2)

        weights.append(w)

    return roots, weights


# Integrate using Gauss-Laguerre
def gauss_laguerre(f, n):

    roots, weights = laguerre_points(n)

    result = 0.0

    for i in range(n):

        result += weights[i] * f(roots[i])

    return result


# -----------------------------------------
# PART B: GAUSS-HERMITE QUADRATURE
# -----------------------------------------

# Function to calculate Hermite polynomial
def hermite(n, x):

    if n == 0:
        return 1.0

    if n == 1:
        return 2.0*x

    h0 = 1.0
    h1 = 2.0*x

    for k in range(2, n + 1):

        h2 = 2*x*h1 - 2*(k-1)*h0

        h0 = h1
        h1 = h2

    return h1


# Calculate Hermite roots and weights
def hermite_points(n):

    limit = max(8.0, 3.0*math.sqrt(2*n+1))

    roots = find_roots(
        lambda x: hermite(n, x),
        -limit, limit, 0.01
    )

    if len(roots) != n:
        raise ValueError("Unable to locate all Hermite roots.")

    weights = []

    for x in roots:

        p = hermite(n-1, x)

        w = ((2**(n-1)) * math.factorial(n)
             * math.sqrt(math.pi)) / (n**2 * p**2)

        weights.append(w)

    return roots, weights


# Integrate using Gauss-Hermite
def gauss_hermite(f, n):

    roots, weights = hermite_points(n)

    result = 0.0

    for i in range(n):

        result += weights[i] * f(roots[i])

    return result


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

def main():

    n = 5

    print("\nIMPROPER INTEGRATION")
    print("================================")

    # GAUSS-LAGUERRE EXAMPLE
    print("\n1. GAUSS-LAGUERRE QUADRATURE")
    print("--------------------------------")

    # Integral: integral of e^(-x)*x^2
    # from 0 to infinity

    f1 = lambda x: x**2

    result1 = gauss_laguerre(f1, n)

    exact1 = 2.0

    print("Integral: Integral from 0 to infinity")
    print("of e^(-x) * x^2 dx")

    print(f"Numerical result = {result1:.10f}")
    print(f"Exact result = {exact1:.10f}")

    print(f"Absolute error = {abs(result1-exact1):.10e}")


    # GAUSS-HERMITE EXAMPLE
    print("\n2. GAUSS-HERMITE QUADRATURE")
    print("--------------------------------")

    # Integral: integral of e^(-x^2)*x^2
    # from minus infinity to infinity

    f2 = lambda x: x**2

    result2 = gauss_hermite(f2, n)

    exact2 = math.sqrt(math.pi) / 2

    print("Integral: Integral from -infinity to +infinity")
    print("of e^(-x^2) * x^2 dx")

    print(f"Numerical result = {result2:.10f}")
    print(f"Exact result = {exact2:.10f}")

    print(f"Absolute error = {abs(result2-exact2):.10e}")


if __name__ == "__main__":
    main()
