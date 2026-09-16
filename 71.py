n = int(input("Enter a decimal number: "))
if n == 0:
    binary = "0"
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
print("Binary:", binary)
