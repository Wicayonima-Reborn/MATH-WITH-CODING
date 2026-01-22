"""
Problem 02 - Turunan Numerik (Finite Difference)

Diketahui:
f(x) = x^3 - 4x^2 + 2x

Ditanyakan:
Nilai turunan f'(x) di x = 2
menggunakan pendekatan numerik.
"""

# ----------------------------------------
# 1. Definisi fungsi matematika
# ----------------------------------------
def f(x):
    """
    Fungsi matematika:
    f(x) = x^3 - 4x^2 + 2x
    """
    return x**3 - 4*x**2 + 2*x


# ----------------------------------------
# 2. Fungsi turunan numerik
# ----------------------------------------
def numerical_derivative(func, x, h=0.0001):
    """
    Menghitung turunan numerik menggunakan
    forward finite difference.

    f'(x) ≈ (f(x + h) - f(x)) / h
    """
    return (func(x + h) - func(x)) / h


# ----------------------------------------
# 3. Nilai turunan analitik (pembanding)
# ----------------------------------------
def analytical_derivative(x):
    """
    Turunan analitik dari:
    f(x) = x^3 - 4x^2 + 2x

    f'(x) = 3x^2 - 8x + 2
    """
    return 3*x**2 - 8*x + 2


# ----------------------------------------
# 4. Eksekusi program
# ----------------------------------------
if __name__ == "__main__":
    x_value = 2
    h_value = 0.0001

    numerical_result = numerical_derivative(f, x_value, h_value)
    analytical_result = analytical_derivative(x_value)

    print("=== Turunan Numerik - Problem 02 ===")
    print(f"Fungsi        : f(x) = x^3 - 4x^2 + 2x")
    print(f"Titik x       : {x_value}")
    print(f"Nilai h       : {h_value}")
    print(f"Hasil numerik : {numerical_result}")
    print(f"Nilai eksak   : {analytical_result}")
    print(f"Error         : {abs(numerical_result - analytical_result)}")
