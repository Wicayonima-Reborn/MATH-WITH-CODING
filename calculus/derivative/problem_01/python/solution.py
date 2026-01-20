def f(x):
    return 3*x*x + 2*x

def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

print(derivative(f, 1))