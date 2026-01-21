"""
Problem 01 - Turunan Numerik (Finite Difference)

Diketahui:
f(x) = 3x^2 + 2x

Ditanyakan:
Nilai turunan f'(x) di x = 1
menggunakan pendekatan numerik.
"""

# ----------------------------------------
# 1. Definisi fungsi matematika
# ----------------------------------------
def f(x):
    """
    Fungsi matematika:
    f(x) = 3x^2 + 2x
    """
    return 3 * x**2 + 2 * x


# ----------------------------------------
# 2. Fungsi turunan numerik
# ----------------------------------------
def numerical_derivative(func, x, h=0.0001):
    """
    Menghitung turunan numerik menggunakan finite difference.

    f'(x) ≈ (f(x + h) - f(x)) / h
    """
    return (func(x + h) - func(x)) / h


# ----------------------------------------
# 3. Eksekusi perhitungan
# ----------------------------------------
if __name__ == "__main__":
    x_value = 1
    h_value = 0.0001

    derivative_value = numerical_derivative(f, x_value, h_value)

    print("=== Turunan Numerik ===")
    print(f"Fungsi      : f(x) = 3x^2 + 2x")
    print(f"Titik x     : {x_value}")
    print(f"Nilai h     : {h_value}")
    print(f"Hasil f'(x) : {derivative_value}")

    # nilai pembanding (analitik)
    exact_value = 6 * x_value + 2
    print(f"Nilai eksak : {exact_value}")
    print(f"Error       : {abs(derivative_value - exact_value)}")
