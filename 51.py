n = int(input("Enter a number: "))
temp = n
reversed_num = 0
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
if n == reversed_num:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
