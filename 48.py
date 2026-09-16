n = int(input("Enter a number: "))
count = 0
temp = abs(n)
if temp == 0:
    count = 1
while temp > 0:
    count += 1
    temp //= 10
print("Number of digits:", count)
