def print_inc_dec(i, n):
    if i > n:
        return
    print(i, end=" ")
    print_inc_dec(i + 1, n)
    print(i, end=" ")

n = int(input("Enter N: "))
print_inc_dec(1, n)
print()
