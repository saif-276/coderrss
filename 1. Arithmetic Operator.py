#1 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)
print("Remainder =", a % b)

#2 
r = float(input("Enter radius: "))

area = 3.14 * r * r

print("Area of the circle =", area)

#3 
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)

#4 
c = float(input("Enter temperature in Celsius: "))

f = (c * 9 / 5) + 32

print("Temperature in Fahrenheit =", f)

#5 
n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by neither 3 nor 5)
