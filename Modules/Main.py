from products import products
from cart import add_to_cart
from billing import calculate_bill

print("Available Products")

for item, price in products.items():
    print(item, "-", price)

cart = add_to_cart(products)

calculate_bill(cart, products)

