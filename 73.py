count = 0
total = 0
while True:
    n = float(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    count += 1
    total += n

if count > 0:
    print("Count:", count)
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered")
