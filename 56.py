n = int(input("Enter a number: "))
is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is {'prime' if is_prime else 'not prime'}")
