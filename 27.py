units = float(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 3
else:
    bill = 100 * 1.5 + 200 * 3 + (units - 300) * 5
print(f"Electricity bill: {bill:.2f}")
