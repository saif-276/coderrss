n = int(input("Enter a number: "))
k = int(input("Enter bit position (0-indexed): "))
if n & (1 << k):
    print(f"Bit {k} is SET")
else:
    print(f"Bit {k} is NOT set")
