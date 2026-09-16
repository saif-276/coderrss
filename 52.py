def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

n = int(input("Enter a number: "))
print(f"{n} is {'a happy' if is_happy(n) else 'not a happy'} number")
