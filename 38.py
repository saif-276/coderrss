n = int(input("Enter a 3-digit number: "))
s = str(n)
total = sum(int(d) ** 3 for d in s)
if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
