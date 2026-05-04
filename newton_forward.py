n = int(input("Enter number of data points: "))
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))
xp = float(input("Enter value to interpolate at: "))

h = x[1] - x[0]
p = (xp - x[0]) / h

diff = [y[:]]
for i in range(1, n):
    col = []
    for j in range(n - i):
        col.append(diff[i-1][j+1] - diff[i-1][j])
    diff.append(col)

result = diff[0][0]
p_term = 1
fact = 1
for i in range(1, n):
    p_term *= (p - (i - 1))
    fact *= i
    result += (p_term / fact) * diff[i][0]

print(f"Interpolated value at x = {xp} is {result}")
