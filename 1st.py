#Arithmetic Operators#

#1 question
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)
print("Remainder =", a % b)

#2 Question
r = float(input("Enter radius: "))

area = 3.14 * r * r

print("Area of the circle =", area)

#3 question
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)

#4 question 
c = float(input("Enter temperature in Celsius: "))

f = (c * 9 / 5) + 32

print("Temperature in Fahrenheit =", f)

#5 question
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by neither 3 nor 5")


#Relational & Logical Operators#

#6 question
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both are equal")

#7 question
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#8 question
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All three numbers are equal")
else:
    print("All three numbers are not equal")

#9 question
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#10 question
ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")
