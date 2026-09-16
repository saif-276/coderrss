x = float(input("Enter x (in radians): "))
n_terms = int(input("Enter number of terms: "))

result = 0
sign = 1
for i in range(n_terms):
    power = 2 * i + 1
    factorial = 1
    for j in range(1, power + 1):
        factorial *= j
    term = (x ** power) / factorial
    result += sign * term
    sign *= -1

print(f"sin({x}) approx = {result:.6f}")
