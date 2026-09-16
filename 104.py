n = int(input("Enter N (even number recommended): "))
size = 2 * n
for i in range(size):
    for j in range(size):
        dist = abs(i - n) + abs(j - n)
        if dist == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
