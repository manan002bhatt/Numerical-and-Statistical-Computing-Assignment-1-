def f(x):
    return x**3 - x - 2

def bisection(a, b, tol=0.0001):
    if f(a) * f(b) >= 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return

    print(f"{'Iter':<6} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12}")
    print("-" * 55)

    iteration = 1
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        print(f"{iteration:<6} {a:<12.6f} {b:<12.6f} {c:<12.6f} {f(c):<12.6f}")
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    root = (a + b) / 2
    print(f"\nApproximate Root: {root:.6f}")
    return root

a = float(input("Enter a: "))
b = float(input("Enter b: "))
bisection(a, b)
