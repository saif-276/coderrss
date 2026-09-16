n = int(input("Enter a number: "))
count = 0
temp = n
while temp:
    count += temp & 1
    temp >>= 1
print(f"Number of set bits in {n}: {count}")
