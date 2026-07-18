def withdraw(balance):
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful!")
    else:
        print("Insufficient Balance!")

    return balance

#balance.py

def check_balance(balance):
    print(f"Current Balance: ₹{balance}")
