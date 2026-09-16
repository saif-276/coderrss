a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
lcm = (a * b) // gcd(a, b)
print("LCM:", lcm)
