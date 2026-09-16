a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    first = a
    second, third = (b, c) if b <= c else (c, b)
elif b <= a and b <= c:
    first = b
    second, third = (a, c) if a <= c else (c, a)
else:
    first = c
    second, third = (a, b) if a <= b else (b, a)

print(f"Ascending order: {first}, {second}, {third}")
