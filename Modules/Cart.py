def add_to_cart(products):
    cart = []

    while True:
        item = input("Enter product name: ").lower()

        if item in products:
            cart.append(item)
            print(item, "added to cart.")
        else:
            print("Product not found!")

        choice = input("Add another item? (yes/no): ").lower()

        if choice == "no":
            break

    return cart
