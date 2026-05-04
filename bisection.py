def f(x):
    return x**3 - x - 2

a = float(input("Enter a: "))
b = float(input("Enter b: "))

if f(a) * f(b) > 0:
    print("f(a) and f(b) must have opposite signs.")
else:
    for i in range(20):
        c = (a + b) / 2
        print(f"Iteration {i+1}: a={a}, b={b}, c={c}, f(c)={f(c)}")
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Root =", (a + b) / 2)
