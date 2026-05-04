def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

x0 = float(input("Enter initial guess: "))

for i in range(10):
    if df(x0) == 0:
        print("Derivative is zero. Method fails.")
        break
    x1 = x0 - f(x0) / df(x0)
    print(f"Iteration {i+1}: x1 = {x1}")
    if abs(x1 - x0) < 0.0001:
        break
    x0 = x1

print("Root =", x1)
