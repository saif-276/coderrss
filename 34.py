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
