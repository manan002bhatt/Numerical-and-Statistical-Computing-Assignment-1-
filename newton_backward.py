def newton_backward(x, y, xp):
    n = len(x)
    h = x[1] - x[0]
    p = (xp - x[-1]) / h

    diff = [y[:]]
    for i in range(1, n):
        col = []
        for j in range(n - i):
            col.append(diff[i-1][j+1] - diff[i-1][j])
        diff.append(col)

    result = diff[0][-1]
    p_term = 1
    factorial = 1
    for i in range(1, n):
        p_term *= (p + (i - 1))
        factorial *= i
        result += (p_term / factorial) * diff[i][-(1)]

    print(f"\nInterpolated value at x = {xp}: {result:.6f}")
    return result

n = int(input("Enter number of data points: "))
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))
xp = float(input("Enter x to interpolate at: "))

newton_backward(x, y, xp)
