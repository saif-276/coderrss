#11
n = int(input("Enter a number: "))
if n & 1 == 0:
    print("Even")
else:
    print("Odd")

#12
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swap: a={a}, b={b}")

#13
n = int(input("Enter a number: "))
print(f"{n} << 1 = {n << 1}  (equivalent to {n} * 2)")
print(f"{n} >> 1 = {n >> 1}  (equivalent to {n} // 2)")

#14
n = int(input("Enter a number: "))
k = int(input("Enter bit position (0-indexed): "))
if n & (1 << k):
    print(f"Bit {k} is SET")
else:
    print(f"Bit {k} is NOT set")

#15
n = int(input("Enter a number: "))
count = 0
temp = n
while temp:
    count += temp & 1
    temp >>= 1
print(f"Number of set bits in {n}: {count}")
