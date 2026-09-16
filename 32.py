n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
