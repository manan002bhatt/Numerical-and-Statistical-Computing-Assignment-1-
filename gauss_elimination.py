def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        A[i] = A[i] + [b[i]]

    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] -= factor * A[i][k]

    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    print("\nSolution:")
    for i in range(n):
        print(f"  x{i+1} = {x[i]:.6f}")
    return x

n = int(input("Enter number of equations: "))
A = []
b = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)
b = list(map(float, input("Enter constants (b): ").split()))

gauss_elimination(A, b)
