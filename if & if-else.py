#16
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#17
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#18
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Largest:", a if a > b else b)

#19
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest:", largest)

#20
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
