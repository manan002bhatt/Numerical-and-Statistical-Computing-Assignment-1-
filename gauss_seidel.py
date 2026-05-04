n = int(input("Enter number of equations: "))

A = []
for i in range(n):
    row = list(map(float, input(f"Enter row {i+1} (coefficients): ").split()))
    A.append(row)

b = list(map(float, input("Enter constants: ").split()))

x = [0.0] * n

for iteration in range(20):
    x_old = x[:]
    for i in range(n):
        total = b[i]
        for j in range(n):
            if j != i:
                total -= A[i][j] * x[j]
        x[i] = total / A[i][i]
    print(f"Iteration {iteration+1}: {x}")
    if all(abs(x[i] - x_old[i]) < 0.0001 for i in range(n)):
        break

print("\nSolution:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")
