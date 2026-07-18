def deposit(balance):
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance = balance + amount
        print("Deposit Successful!")
    else:
        print("Invalid amount!")

    return balance
