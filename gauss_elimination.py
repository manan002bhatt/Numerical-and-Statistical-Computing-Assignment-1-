n = int(input("Enter number of equations: "))

A = []
for i in range(n):
    row = list(map(float, input(f"Enter row {i+1} (coefficients and constant): ").split()))
    A.append(row)

for i in range(n):
    for j in range(i+1, n):
        ratio = A[j][i] / A[i][i]
        for k in range(n+1):
            A[j][k] -= ratio * A[i][k]

x = [0] * n
for i in range(n-1, -1, -1):
    x[i] = A[i][n]
    for j in range(i+1, n):
        x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]

print("\nSolution:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")
