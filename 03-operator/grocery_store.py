product_1=input("product:")
price_1=float(input("price:"))

product_2=input("product:")
price_2=float(input("price:"))


product_3=input("product:")
price_3=float(input("price:"))

discount=int(input("discount="))

bill=price_1+price_2+price_3
discount_amt=(bill*discount)/100
final_bill=bill-discount_amt
yes_or_no=(final_bill>1000)

print(f"product:{product_1}:{price_1}")
print(f"product:{product_2}:{price_2}")
print(f"product:{product_3}:{price_3}")
print(f"bill:{bill}")
print(f"dicount amount:{discount_amt}")
print(f"final bill:{final_bill}")
print(f"your bill > 1000:{yes_or_no}")
