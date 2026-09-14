#30
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        print("Result:", a / b if b != 0 else "Error: division by zero")
    case _:
        print("Invalid operator")

#31
month = int(input("Enter month number (1-12): "))
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                  7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if month in days_in_month:
    print(f"Days: {days_in_month[month]}")
else:
    print("Invalid month")

#32
n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#33
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


#34
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate discriminant
d = b * b - 4 * a * c

print("Discriminant =", d)

if d > 0:
    print("Roots are real and unequal")

    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)

    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    print("Roots are real and equal")

    root = -b / (2 * a)

    print("Root 1 =", root)
    print("Root 2 =", root)

else:
    print("Roots are imaginary")

    real_part = -b / (2 * a)
    imaginary_part = (-d) ** 0.5 / (2 * a)

    print("Root 1 =", real_part, "+", imaginary_part, "i")
    print("Root 2 =", real_part, "-", imaginary_part, "i")
