def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol=0.0001):
    print(f"{'Iter':<6} {'x0':<15} {'f(x0)':<15} {'f\'(x0)':<15} {'x1':<15}")
    print("-" * 65)

    for i in range(1, 100):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Derivative is zero. Method fails.")
            return
        x1 = x0 - fx / dfx
        print(f"{i:<6} {x0:<15.6f} {fx:<15.6f} {dfx:<15.6f} {x1:<15.6f}")
        if abs(x1 - x0) < tol:
            break
        x0 = x1

    print(f"\nApproximate Root: {x1:.6f}")
    return x1

x0 = float(input("Enter initial guess x0: "))
newton_raphson(x0)
