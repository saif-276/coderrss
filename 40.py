balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
MIN_BALANCE = 500

if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif balance - amount < MIN_BALANCE:
    print("Transaction declined: insufficient balance (minimum balance rule)")
else:
    balance -= amount
    print(f"Withdrawal successful. New balance: {balance:.2f}")
