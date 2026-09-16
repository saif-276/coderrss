n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print(f"{n} is {'a perfect' if total == n else 'not a perfect'} number")
