def jacobi(A, b, tol=0.0001, max_iter=100):
    n = len(b)
    x = [0.0] * n

    print(f"{'Iter':<6} " + " ".join(f"{'x'+str(i+1):<12}" for i in range(n)))
    print("-" * (6 + 12 * n))

    for iteration in range(1, max_iter + 1):
        x_new = [0.0] * n
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]

        print(f"{iteration:<6} " + " ".join(f"{xi:<12.6f}" for xi in x_new))

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            break
        x = x_new[:]

    print("\nSolution:")
    for i in range(n):
        print(f"  x{i+1} = {x_new[i]:.6f}")
    return x_new

n = int(input("Enter number of equations: "))
A = []
b = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)
b = list(map(float, input("Enter constants (b): ").split()))

jacobi(A, b)
