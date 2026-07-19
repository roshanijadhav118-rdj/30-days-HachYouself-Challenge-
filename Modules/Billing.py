def calculate_bill(cart, products):
    bill = 0

    print("\nItems in Cart:")
    for item in cart:
        print(item, "-", products[item])
        bill += products[item]

    print("\nTotal Bill =", bill)

    if bill > 5000:
        discount = bill * 10 / 100
        final_bill = bill - discount

        print("Discount =", discount)
        print("Final Bill =", final_bill)
    else:
        print("No Discount")
