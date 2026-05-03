def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=0.0001):
    if f(a) * f(b) >= 0:
        print("Invalid interval.")
        return

    print(f"{'Iter':<6} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12}")
    print("-" * 55)

    for i in range(1, 100):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{i:<6} {a:<12.6f} {b:<12.6f} {c:<12.6f} {f(c):<12.6f}")
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f"\nApproximate Root: {c:.6f}")
    return c

a = float(input("Enter a: "))
b = float(input("Enter b: "))
regula_falsi(a, b)
